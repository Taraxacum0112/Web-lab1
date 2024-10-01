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
        self.server_socket = None
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
            self.server_socket.close()
        self.ui.button_run.setText("Запустить")
        self.ui.label_status.setText("Статус: не подключён")

    def run_server(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.ip, self.port))
            self.server_socket.listen(1)
            print(f'Сервер запущен на {self.ip}:{self.port}, ожидание подключения...')
            while self.is_running:
                connection, address = self.server_socket.accept()
                print(f'Клиент подключен: {address}')
                self.ui.label_status.setText("Статус: подключён")
                try:
                    while self.is_running:
                        data = connection.recv(1024).decode()
                        if not data:
                            break
                        print(f'Сообщение от клиента: {data}')
                except:
                    pass
                connection.close()
                print("Клиент отключился")
                self.ui.label_status.setText("Статус: не подключён")
        except Exception as e:
            print(f'Ошибка: {str(e)}')
        finally:
            if self.server_socket:
                self.server_socket.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ServerWindow()
    window.show()
    sys.exit(app.exec_())
