import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from client_ui import Ui_MainWindow

class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClientWindow()
    window.show()
    sys.exit(app.exec_())
