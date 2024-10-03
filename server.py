import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.server_ui import Ui_MainWindow

CLIENT_COLORS = ['blue', 'orange', 'brown', 'purple', 'gray']


class ServerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Сервер")
        self.ui.button_run.clicked.connect(self.toggle_server)
        self.ui.button_send.clicked.connect(self.send_server_message)
        self.server_socket = None
        self.clients = {}
        self.client_colors = {}
        self.is_running = False
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 10000
        self.ui.label_ip.setText(f'IP: {self.ip}')
        self.update_status_label("не подключён", "red")
        self.color_index = 0

    def toggle_server(self):
        if not self.is_running:
            self.start_server()
        else:
            self.stop_server()

    def start_server(self):
        self.ui.button_run.setText("Остановить")
        self.is_running = True
        self.update_status_label("не подключён", "red")
        self.server_thread = threading.Thread(target=self.run_server)
        self.server_thread.start()

    def stop_server(self):
        if self.server_socket:
            self.is_running = False
            for client_socket in self.clients:
                client_socket.close()
            self.server_socket.close()
            self.ui.textBrowser.append('<i>Сервер остановлен</i>')
        self.ui.button_run.setText("Запустить")
        self.update_status_label("не подключён", "red")

    def run_server(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.ip, self.port))
            self.server_socket.listen(5)
            self.ui.textBrowser.append('<i>Сервер запущен, ожидание подключения...</i>')
            while self.is_running:
                client_socket, address = self.server_socket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
        except Exception as e:
            print(f'Ошибка: {str(e)}')
        finally:
            if self.server_socket:
                self.server_socket.close()

    def handle_client(self, client_socket):
        try:
            nickname = client_socket.recv(1024).decode()
            self.clients[client_socket] = nickname

            color = CLIENT_COLORS[self.color_index % len(CLIENT_COLORS)]
            self.client_colors[nickname] = color
            self.color_index += 1

            client_socket.sendall(f"COLOR:{color}".encode())

            self.broadcast_message(f'<i><span style="color: {color};">{nickname}</span> <span style="color: black;">присоединился к чату</span></i>',None)

            self.update_status_label("подключён", "green")

            while True:
                data = client_socket.recv(1024).decode()
                if data:
                    formatted_message = f'<span style="color: {color};">{nickname}:</span> <span style="color: black;">{data}</span>'
                    self.broadcast_message(formatted_message, client_socket)
        except:
            self.disconnect_client(client_socket)
        finally:
            client_socket.close()

    def broadcast_message(self, message, sender_socket):
        for client_socket in self.clients:
            try:
                client_socket.sendall(message.encode())
            except:
                self.disconnect_client(client_socket)

        if sender_socket:
            self.ui.textBrowser.append(message)
        else:
            self.ui.textBrowser.append(f'<span style="color: red;">{message}</span>')

    def send_server_message(self):
        message = self.ui.line_message.text()
        if message:
            formatted_message = f'<span style="color: red;">Сервер:</span> <span style="color: black;">{message}</span>'
            self.broadcast_message(formatted_message, None)
            self.ui.line_message.clear()

    def disconnect_client(self, client_socket):
        nickname = self.clients.pop(client_socket, None)
        if nickname:
            color = self.client_colors.get(nickname, "black")
            self.broadcast_message(
                f'<i><span style="color: {color};">{nickname}</span> <span style="color: black;">покинул чат</span></i>',
                None)
        client_socket.close()

        if not self.clients:
            self.update_status_label("не подключён", "red")

    def update_status_label(self, status_text, color):
        formatted_text = f'Статус: <span style="color: {color};">{status_text}</span>'
        self.ui.label_status.setText(formatted_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ServerWindow()
    window.show()
    sys.exit(app.exec_())