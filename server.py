import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from server_ui import Ui_MainWindow

class ServerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ServerWindow()
    window.show()
    sys.exit(app.exec_())
