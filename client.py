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
            print(f'Подключено к серверу на {ip}:{port}')
        except Exception as e:
            print(f'Ошибка подключения: {str(e)}')
            self.ui.label_status.setText("Ошибка подключения")

    def disconnect_from_server(self):
        if self.client_socket:
            self.client_socket.close()
        self.is_connected = False
        self.ui.label_status.setText("Статус: не подключён")
        self.ui.button_connect.setText("Подключиться")
        print("Отключено от сервера")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClientWindow()
    window.show()
    sys.exit(app.exec_())
