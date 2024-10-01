import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from server_ui import Ui_MainWindow

class ServerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Сервер")
        self.ui.button_run.clicked.connect(self.toggle_server)
        self.ui.button_send.clicked.connect(self.send_message)
        self.server_socket = None
        self.connection = None
        self.is_running = False
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 10000
        self.ui.label_ip.setText(f'IP: {self.ip}')
        self.update_status_label("не подключён", "red")

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
            if self.connection:
                self.connection.close()
            self.server_socket.close()
            self.ui.textBrowser.append('<i>Сервер остановлен</i>')
        self.ui.button_run.setText("Запустить")
        self.update_status_label("не подключён", "red")

    def run_server(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.ip, self.port))
            self.server_socket.listen(1)
            self.ui.textBrowser.append('<i>Сервер запущен, ожидание подключения...</i>')
            while self.is_running:
                self.connection, address = self.server_socket.accept()
                self.update_status_label("подключён", "green")
                self.ui.textBrowser.append('<i>Клиент подключен</i>')
                receive_thread = threading.Thread(target=self.receive_message)
                receive_thread.start()
        except Exception as e:
            print(f'Ошибка: {str(e)}')
        finally:
            if self.server_socket:
                self.server_socket.close()

    def send_message(self):
        if self.connection:
            message = self.ui.line_message.text()
            if message:
                formatted_message = f'<span style="color: red;">Сервер:</span> {message}'
                self.ui.textBrowser.append(formatted_message)
                self.connection.sendall(f'Сервер: {message}'.encode())
                self.ui.line_message.clear()
        else:
            self.ui.textBrowser.append("Сообщение не отправлено: нет подключения к клиенту")

    def receive_message(self):
        try:
            while self.is_running:
                try:
                    data = self.connection.recv(1024).decode()
                    if data:
                        formatted_message = f'<span style="color: green;">Клиент:</span> {data.split(": ", 1)[1]}'
                        self.ui.textBrowser.append(formatted_message)
                    else:
                        break
                except ConnectionResetError:
                    break
        except Exception as e:
            print(f'Ошибка получения данных: {str(e)}')
        finally:
            if self.connection:
                self.ui.textBrowser.append('<i>Клиент отключился</i>')
                self.connection.close()
            self.connection = None
            self.update_status_label("не подключён", "red")

    def update_status_label(self, status_text, color):
        formatted_text = f'Статус: <span style="color: {color};">{status_text}</span>'
        self.ui.label_status.setText(formatted_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ServerWindow()
    window.show()
    sys.exit(app.exec_())