import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from server_ui import Ui_MainWindow
import socket

class ServerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def start_server():
    HOST = (ip, port)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(HOST)

    server.listen()
    print('Start listening')

    connection, address = server.accept()
    print(f'New connection from {address}')
    
    while 1:
        data = connection.recv(1024).decode()
        print(data) # поменять на вывод в окно сообщений
    
    connection.close()
    server.close()

ip = socket.gethostbyname(socket.gethostname())
port = 10000    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ServerWindow()
    window.show()
    sys.exit(app.exec_())
