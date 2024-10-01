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

        # Привязываем кнопку запуска сервера
        self.ui.button_run.clicked.connect(self.start_server)

        # Инициализация серверного сокета
        self.server_socket = None
        self.ip = socket.gethostbyname(socket.gethostname())  # Получаем локальный IP-адрес
        self.port = 10000

        # Отображаем IP-адрес в label_ip
        self.ui.label_ip.setText(f'IP: {self.ip}')

    def start_server(self):
        # Запускаем сервер в отдельном потоке
        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

    def run_server(self):
        try:
            # Создаем серверный сокет
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.ip, self.port))
            self.server_socket.listen(1)  # Ожидаем одно подключение
            print(f'Сервер запущен на {self.ip}:{self.port}, ожидание подключения...')

            # Принимаем подключение от клиента
            connection, address = self.server_socket.accept()
            print(f'Клиент подключен: {address}')

        except Exception as e:
            print(f'Ошибка: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ServerWindow()
    window.show()
    sys.exit(app.exec_())
