import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from client_ui import Ui_MainWindow
import socket

class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def connect (): # по нажатию кнопки подключиться
    full_text = window.ui.line_ip.text()
    ip = full_text.replace('IP: ', '').strip()
    port = 10000
    if (ip_is_valid(ip) and port != ""):
        socket.connect((ip, int(port)))
    else:
        print(f"IP адресс должен быть в формате xxx.xxx.xxx.xxx")
        #надо бы добавить выскакивающее окно ошибки
        #error_ip.config(text="IP адресс должен быть в формате xxx.xxx.xxx.xxx")

def ip_is_valid (ip):
    try:
        host_bytes = ip.split('.')
        valid = [int(b) for b in host_bytes]
        valid = [b for b in valid if b>=0 and b<=255]
        return len(host_bytes) == 4 and len(valid) == 4
    except:
        return False  
    
def send_message (): #по нажатию кнопки отправить
    data = window.ui.line_message.text()
    socket.sendall(data.encode())
    
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClientWindow()
    window.show()
    sys.exit(app.exec_())
