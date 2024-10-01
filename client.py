import sys
import socket
from PyQt5.QtWidgets import QApplication, QMainWindow
from client_ui import Ui_MainWindow

class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Привязываем кнопку подключения к серверу
        self.ui.button_connect.clicked.connect(self.connect_to_server)

        # Инициализация клиентского сокета
        self.client_socket = None

    def connect_to_server(self):
        # Получаем IP-адрес из line_ip
        full_text = self.ui.line_ip.text()
        ip = full_text.replace('IP: ', '').strip()
        port = 10000  # Используем тот же порт, что и на сервере

        try:
            # Создаем клиентский сокет и подключаемся к серверу
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip, port))
            print(f'Подключено к серверу на {ip}:{port}')

        except Exception as e:
            print(f'Ошибка подключения: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClientWindow()
    window.show()
    sys.exit(app.exec_())
