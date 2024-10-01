import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from client_ui import Ui_MainWindow

class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_connect.clicked.connect(self.toggle_connection)
        self.ui.button_send.clicked.connect(self.send_message)
        self.client_socket = None
        self.is_connected = False
        self.ui.label_status.setText("Статус: не подключён")

    def toggle_connection(self):
        if not self.is_connected:
            self.connect_to_server()
        else:
            self.disconnect_from_server()

    def connect_to_server(self):
        full_text = self.ui.line_ip.text()
        ip = full_text.replace('IP: ', '').strip()
        port = 10000
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip, port))
            self.is_connected = True
            self.ui.label_status.setText("Статус: подключён")
            self.ui.button_connect.setText("Отключиться")
            self.ui.textBrowser.append('Подключено к серверу')
            receive_thread = threading.Thread(target=self.receive_message)
            receive_thread.start()
        except Exception as e:
            print(f'Ошибка подключения: {str(e)}')
            self.ui.label_status.setText("Ошибка подключения")

    def send_message(self):
        if self.client_socket and self.is_connected:
            message = self.ui.line_message.text()
            if message:
                self.ui.textBrowser.append(f'Клиент: {message}')
                self.client_socket.sendall(f'Клиент: {message}'.encode())
                self.ui.line_message.clear()
        else:
            self.ui.textBrowser.append("Сообщение не отправлено: нет подключения к серверу")

    def receive_message(self):
        try:
            while self.is_connected:
                data = self.client_socket.recv(1024).decode()
                if data:
                    self.ui.textBrowser.append(data)
                else:
                    self.ui.textBrowser.append("Соединение с сервером потеряно")
                    break
        except:
            pass
        finally:
            self.disconnect_from_server()

    def disconnect_from_server(self):
        if self.client_socket:
            self.client_socket.close()
        self.is_connected = False
        self.ui.label_status.setText("Статус: не подключён")
        self.ui.button_connect.setText("Подключиться")
        self.ui.textBrowser.append("Отключено от сервера")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClientWindow()
    window.show()
    sys.exit(app.exec_())