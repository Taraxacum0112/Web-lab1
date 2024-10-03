import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from ui.client_ui import Ui_MainWindow
from ui.windnick_ui import Ui_Dialog

class NicknameDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.button_ok.clicked.connect(self.submit_nickname)
        self.nickname = None

    def submit_nickname(self):
        self.nickname = self.ui.line_nickname.text()
        if self.nickname:
            self.accept()

class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Клиент")
        self.ui.button_connect.clicked.connect(self.toggle_connection)
        self.ui.button_send.clicked.connect(self.send_message)
        self.client_socket = None
        self.is_connected = False
        self.nickname = None
        self.assigned_color = None
        self.update_status_label("не подключён", "red")

    def toggle_connection(self):
        if not self.is_connected:
            self.open_nickname_dialog()
        else:
            self.disconnect_from_server()

    def open_nickname_dialog(self):
        dialog = NicknameDialog()
        if dialog.exec_():
            self.nickname = dialog.nickname
            self.connect_to_server()

    def connect_to_server(self):
        full_text = self.ui.line_ip.text()
        ip = full_text.replace('IP: ', '').strip()
        port = 10000
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip, port))
            self.client_socket.sendall(self.nickname.encode())
            self.is_connected = True
            self.update_status_label("подключён", "green")
            self.ui.button_connect.setText("Отключиться")
            self.ui.textBrowser.append(f'<i>Подключено к серверу как {self.nickname}</i>')
            receive_thread = threading.Thread(target=self.receive_message)
            receive_thread.start()
        except (socket.error, ConnectionRefusedError) as e:
            self.update_status_label("Ошибка подключения", "red")
            print(f'Ошибка подключения: {str(e)}')

    def send_message(self):
        if self.client_socket and self.is_connected:
            message = self.ui.line_message.text()
            if message:
                formatted_message = f'<span style="color: green;">{self.nickname}:</span> {message}'
                self.ui.textBrowser.append(formatted_message)
                self.client_socket.sendall(message.encode())
                self.ui.line_message.clear()
        else:
            self.ui.textBrowser.append("Сообщение не отправлено: нет подключения к серверу")

    def receive_message(self):
        try:
            while self.is_connected:
                data = self.client_socket.recv(1024).decode()
                if data.startswith("COLOR:"):
                    self.assigned_color = data.split(":")[1]
                else:
                    if f'{self.nickname}:' not in data:
                        self.ui.textBrowser.append(data)
        except:
            pass
        finally:
            if self.is_connected:
                self.disconnect_from_server()

    def disconnect_from_server(self):
        if self.client_socket:
            self.client_socket.close()
        self.is_connected = False
        self.update_status_label("не подключён", "red")
        self.ui.button_connect.setText("Подключиться")
        self.ui.textBrowser.append('<i>Отключено от сервера</i>')

    def update_status_label(self, status_text, color):
        formatted_text = f'Статус: <span style="color: {color};">{status_text}</span>'
        self.ui.label_status.setText(formatted_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClientWindow()
    window.show()
    sys.exit(app.exec_())