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
        self.ui.button_run.clicked.connect(self.toggle_server)
        self.ui.button_send.clicked.connect(self.send_message)
        self.server_socket = None
        self.connection = None
        self.is_running = False
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 10000
        self.ui.label_ip.setText(f'IP: {self.ip}')
        self.ui.label_status.setText("Статус: не подключён")

    def toggle_server(self):
        if not self.is_running:
            self.start_server()
        else:
            self.stop_server()

    def start_server(self):
        self.ui.button_run.setText("Остановить")
        self.is_running = True
        self.ui.label_status.setText("Статус: не подключён")
        self.server_thread = threading.Thread(target=self.run_server)
        self.server_thread.start()

    def stop_server(self):
        if self.server_socket:
            self.is_running = False
            if self.connection:
                self.connection.close()
            self.server_socket.close()
            self.ui.textBrowser.append("Сервер остановлен")
        self.ui.button_run.setText("Запустить")
        self.ui.label_status.setText("Статус: не подключён")

    def run_server(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.ip, self.port))
            self.server_socket.listen(1)
            self.ui.textBrowser.append('Сервер запущен, ожидание подключения...')
            while self.is_running:
                self.connection, address = self.server_socket.accept()
                self.ui.label_status.setText("Статус: подключён")
                self.ui.textBrowser.append('Клиент подключен')
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
                self.ui.textBrowser.append(f'Сервер: {message}')
                self.connection.sendall(f'Сервер: {message}'.encode())
                self.ui.line_message.clear()
        else:
            self.ui.textBrowser.append("Сообщение не отправлено: нет подключения к клиенту")

    def receive_message(self):
        try:
            while self.is_running:
                data = self.connection.recv(1024).decode()
                if data:
                    self.ui.textBrowser.append(data)
                else:
                    self.ui.textBrowser.append("Клиент отключился")
                    break
        except:
            pass
        finally:
            self.connection = None
            self.ui.label_status.setText("Статус: не подключён")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ServerWindow()
    window.show()
    sys.exit(app.exec_())
