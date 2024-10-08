import sys
import socket
import threading
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QGridLayout, QVBoxLayout

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

class EmojiDialog(QDialog):
    def __init__(self, parent=None):
        super(EmojiDialog, self).__init__(parent)
        self.setWindowTitle('Выбор смайликов')
        self.setWindowIcon(QIcon('image/icon_wsmiley.png'))

        self.layout = QVBoxLayout()
        grid_layout = QGridLayout()

        self.emoji_list = {
            '😊': ':smile:', '😢': ':sad:', '😂': ':laugh:', '😎': ':cool:', '😭': ':cry:',
            '😍': ':love:', '😡': ':angry:', '🤔': ':think:', '😘': ':kiss:', '🤩': ':star_struck:',
            '🫡': ':salute:', '🫢': ':surprised:', '🫣': ':peek:', '🤨': ':raised_eyebrow:',
            '😐': ':neutral:', '😴': ':sleeping:', '🤤': ':drooling:', '🤮': ':vomit:',
            '🤯': ':exploding_head:', '😷': ':mask:', '🥳': ':party:', '🤓': ':nerd:', '🥹': ':tears_of_joy:',
            '👿': ':imp:', '😈': ':devil:', '🤬': ':cursing:', '😇': ':angel:', '🙃': ':upside_down:',
            '👋': ':wave:', '👌': ':ok:', '🤙': ':call:', '🤟': ':rock:', '🤌': ':pinched:',
            '👆': ':up:', '👇': ':down:', '👈': ':left:', '👉': ':right:', '🖕': ':middle_finger:',
            '👎': ':thumb_down:', '👍': ':thumbsup:', '🙏': ':pray:', '🤝': ':handshake:',
            '💅': ':nails:', '💪': ':muscle:',
            '❤️': ':heart:', '💩': ':poop:', '👾': ':alien:', '👀': ':eyes:',
            '🤰': ':pregnant:', '🥷': ':ninja:', '💃': ':dancer:', '🌹': ':rose:',
            '🌸': ':blossom:', '🥀': ':wilted:', '🐺': ':wolf:', '🍺': ':beer:', '🍷': ':wine:',
            '✨': ':sparkles:', '💸': ':money_with_wings:', '📈': ':chart_up:', '📉': ':chart_down:',
            '🗿': ':moai:', '🐱': ':cat:', '📚': ':book:'
        }

        row, col = 0, 0

        for emoji, code in self.emoji_list.items():
            button = QPushButton(emoji)
            button.setFixedSize(40, 40)
            button.setStyleSheet("""
                QPushButton {
                    background-color: rgb(255, 255, 255); 
                    border-radius: 15px;
                    padding: 5px;
                    font-size: 14pt;
                }
                QPushButton:hover {
                    background-color: rgb(230, 230, 230);
                }
            """)
            button.clicked.connect(lambda _, e=code: self.select_emoji(e))

            grid_layout.addWidget(button, row, col)
            col += 1
            if col > 7:
                col = 0
                row += 1

        self.layout.addLayout(grid_layout)
        self.setLayout(self.layout)
        self.setGeometry(100, 100, 350, 350)

    def select_emoji(self, emoji_code):
        self.accept()
        self.selected_emoji = emoji_code

    def get_selected_emoji(self):
        return getattr(self, 'selected_emoji', None)

class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Клиент")
        self.ui.button_connect.clicked.connect(self.toggle_connection)
        self.ui.button_send.clicked.connect(self.send_message)
        self.ui.button_smiley.clicked.connect(self.open_emoji_dialog)

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

    def open_emoji_dialog(self):
        emoji_dialog = EmojiDialog(self)
        if emoji_dialog.exec_():
            emoji_code = emoji_dialog.get_selected_emoji()
            if emoji_code:
                current_text = self.ui.line_message.text()
                self.ui.line_message.setText(current_text + emoji_code)

    def send_message(self):
        if self.client_socket and self.is_connected:
            message = self.ui.line_message.text()
            if message:
                formatted_message = f'<span style="color: green;">{self.nickname}:</span> {self.replace_emoji_codes(message)}'
                self.ui.textBrowser.append(formatted_message)
                self.client_socket.sendall(message.encode())
                self.ui.line_message.clear()
        else:
            self.ui.textBrowser.append("Сообщение не отправлено: нет подключения к серверу")

    def replace_emoji_codes(self, message):
        emoji_dict = {
            ':smile:': '😊', ':sad:': '😢', ':laugh:': '😂', ':heart:': '❤️', ':thumbsup:': '👍',
            ':poop:': '💩', ':alien:': '👾', ':eyes:': '👀', ':cool:': '😎', ':cry:': '😭',
            ':love:': '😍', ':angry:': '😡', ':think:': '🤔', ':kiss:': '😘', ':star_struck:': '🤩',
            ':salute:': '🫡', ':surprised:': '🫢', ':peek:': '🫣', ':raised_eyebrow:': '🤨', ':neutral:': '😐',
            ':sleeping:': '😴', ':drooling:': '🤤', ':vomit:': '🤮', ':exploding_head:': '🤯', ':mask:': '😷',
            ':party:': '🥳', ':nerd:': '🤓', ':tears_of_joy:': '🥹', ':imp:': '👿', ':devil:': '😈',
            ':cursing:': '🤬', ':angel:': '😇', ':upside_down:': '🙃', ':wave:': '👋', ':ok:': '👌',
            ':call:': '🤙', ':rock:': '🤟', ':pinched:': '🤌', ':up:': '👆', ':down:': '👇',
            ':left:': '👈', ':right:': '👉', ':middle_finger:': '🖕', ':thumb_down:': '👎', ':pray:': '🙏',
            ':handshake:': '🤝', ':nails:': '💅', ':muscle:': '💪', ':pregnant:': '🤰', ':ninja:': '🥷',
            ':dancer:': '💃', ':rose:': '🌹', ':blossom:': '🌸', ':wilted:': '🥀', ':wolf:': '🐺',
            ':beer:': '🍺', ':wine:': '🍷', ':sparkles:': '✨', ':money_with_wings:': '💸', ':chart_up:': '📈',
            ':chart_down:': '📉', ':moai:': '🗿', ':cat:': '🐱', ':book:': '📚'
        }
        for code, emoji in emoji_dict.items():
            message = message.replace(code, emoji)
        return message

    def receive_message(self):
        try:
            while self.is_connected:
                data = self.client_socket.recv(1024).decode()
                if data.startswith("COLOR:"):
                    self.assigned_color = data.split(":")[1]
                else:
                    formatted_message = self.replace_emoji_codes(data)
                    if f'{self.nickname}:' not in formatted_message:
                        self.ui.textBrowser.append(formatted_message)
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