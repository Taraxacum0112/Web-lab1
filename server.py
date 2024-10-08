import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QPushButton, QGridLayout, QVBoxLayout
from ui.server_ui import Ui_MainWindow

CLIENT_COLORS = ['blue', 'orange', 'brown', 'purple', 'gray']

class EmojiDialog(QDialog):
    def __init__(self, parent=None):
        super(EmojiDialog, self).__init__(parent)
        self.setWindowTitle('Выбор смайликов')

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
            '💅': ':nails:', '💪': ':muscle:', '❤️': ':heart:', '💩': ':poop:', '👾': ':alien:', '👀': ':eyes:',
            '🤰': ':pregnant:', '🥷': ':ninja:', '💃': ':dancer:', '🌹': ':rose:', '🌸': ':blossom:',
            '🥀': ':wilted:', '🐺': ':wolf:', '🍺': ':beer:', '🍷': ':wine:', '✨': ':sparkles:',
            '💸': ':money_with_wings:', '📈': ':chart_up:', '📉': ':chart_down:', '🗿': ':moai:',
            '🐱': ':cat:', '📚': ':book:'
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


class ServerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Сервер")
        self.ui.button_run.clicked.connect(self.toggle_server)
        self.ui.button_send.clicked.connect(self.send_server_message)
        self.ui.button_smiley.clicked.connect(self.open_emoji_dialog)  # Добавляем обработчик для выбора смайликов
        self.ui.button_clip.clicked.connect(self.send_picture)
        self.server_socket = None
        self.clients = {}
        self.client_colors = {}
        self.is_running = False
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 10000
        self.ui.label_ip.setText(f'IP: {self.ip}')
        self.update_status_label("не подключён", "red")
        self.color_index = 0
        self.path = None

    def toggle_server(self):
        if not self.is_running:
            self.start_server()
        else:
            self.stop_server()

    def start_server(self):
        self.ui.button_run.setText("Остановить")
        self.is_running = True
        self.update_status_label("не подключён", "red")
        self.server_thread = threading.Thread(target=self.run_server)
        self.server_thread.start()

    def stop_server(self):
        if self.server_socket:
            self.is_running = False
            for client_socket in self.clients:
                client_socket.close()
            self.server_socket.close()
            self.ui.textBrowser.append('<i>Сервер остановлен</i>')
        self.ui.button_run.setText("Запустить")
        self.update_status_label("не подключён", "red")

    def run_server(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.ip, self.port))
            self.server_socket.listen(5)
            self.ui.textBrowser.append('<i>Сервер запущен, ожидание подключения...</i>')
            while self.is_running:
                client_socket, address = self.server_socket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
        except Exception as e:
            print(f'Ошибка: {str(e)}')
        finally:
            if self.server_socket:
                self.server_socket.close()

    def handle_client(self, client_socket):
        try:
            nickname = client_socket.recv(1024).decode()
            self.clients[client_socket] = nickname

            color = CLIENT_COLORS[self.color_index % len(CLIENT_COLORS)]
            self.client_colors[nickname] = color
            self.color_index += 1

            client_socket.sendall(f"COLOR:{color}".encode())

            self.broadcast_message(f'<i><span style="color: {color};">{nickname}</span> <span style="color: black;">присоединился к чату</span></i>', None)

            self.update_status_label("подключён", "green")

            while True:
                data = client_socket.recv(1024).decode()
                if data:
                    formatted_message = f'<span style="color: {color};">{nickname}:</span> <span style="color: black;">{self.replace_emoji_codes(data)}</span>'
                    self.broadcast_message(formatted_message, client_socket)
        except:
            self.disconnect_client(client_socket)
        finally:
            client_socket.close()

    def broadcast_message(self, message, sender_socket):
        for client_socket in self.clients:
            try:
                client_socket.sendall(message.encode())
            except:
                self.disconnect_client(client_socket)

        if sender_socket:
            self.ui.textBrowser.append(message)
        else:
            self.ui.textBrowser.append(f'<span style="color: red;">{message}</span>')

    def send_server_message(self):
        message = self.ui.line_message.text()
        if message:
            formatted_message = f'<span style="color: red;">Сервер:</span> <span style="color: black;">{self.replace_emoji_codes(message)}</span>'
            self.broadcast_message(formatted_message, None)
            self.ui.line_message.clear()

    def open_emoji_dialog(self):
        emoji_dialog = EmojiDialog(self)
        if emoji_dialog.exec_():
            emoji_code = emoji_dialog.get_selected_emoji()
            if emoji_code:
                current_text = self.ui.line_message.text()
                self.ui.line_message.setText(current_text + emoji_code)

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
    
    def send_picture(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        
        if (self.clients):
            for client_socket in self.clients:
                try:
                    data = f'PICTURE:{self.path}:' f'<span style="color: red;">Сервер:</span>'
                    file = open(self.path, mode="rb")
                    client_socket.sendall(data.encode())
    
                    data = file.read(1024)
                    while data:
                        client_socket.send(data)
                        data = file.read(1024)
                    file.close()
                except:
                    self.disconnect_client(client_socket)
        self.ui.textBrowser.append(f'<span style="color: red;">Сервер:</span> <img height="300" width="300" src="{self.path}">')

    def disconnect_client(self, client_socket):
        nickname = self.clients.pop(client_socket, None)
        if nickname:
            color = self.client_colors.get(nickname, "black")
            self.broadcast_message(
                f'<i><span style="color: {color};">{nickname}</span> <span style="color: black;">покинул чат</span></i>',
                None)
        client_socket.close()

        if not self.clients:
            self.update_status_label("не подключён", "red")

    def update_status_label(self, status_text, color):
        formatted_text = f'Статус: <span style="color: {color};">{status_text}</span>'
        self.ui.label_status.setText(formatted_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ServerWindow()
    window.show()
    sys.exit(app.exec_())