from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 500)
        MainWindow.setStyleSheet("background-color: rgb(0, 103, 177);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 531, 481))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_ip = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(12)
        self.line_ip.setFont(font)
        self.line_ip.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 10px;               \n"
"    padding: 10px;                 \n"
"    color: rgb(0, 0, 0);             \n"
"}")
        self.line_ip.setObjectName("line_ip")
        self.horizontalLayout.addWidget(self.line_ip)
        self.label_status = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(12)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("QLabel {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 10px;               \n"
"    padding: 10px;                 \n"
"    color: rgb(0, 0, 0);             \n"
"}\n"
"")
        self.label_status.setObjectName("label_status")
        self.horizontalLayout.addWidget(self.label_status)
        self.button_connect = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_connect.setFont(font)
        self.button_connect.setStyleSheet("QPushButton {\n"
"    background-color: rgb(227, 24, 55);       /* Красный фон в обычном состоянии */\n"
"    border-radius: 10px;                      /* Закругленные углы */\n"
"    padding: 10px;                            /* Внутренние отступы */\n"
"    color: rgb(255, 255, 255);                /* Белый текст */\n"
"    border: 2px solid rgb(227, 24, 55);       /* Красная рамка */\n"
"    font-weight: bold;                        /* Жирный текст */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 20, 50);       /* Темно-красный фон при наведении */\n"
"    color: rgb(255, 255, 255);                /* Белый текст */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 20, 45);       /* Более темный красный при нажатии */\n"
"    color: rgb(255, 255, 255);                /* Белый текст */\n"
"}\n"
"")
        self.button_connect.setObjectName("button_connect")
        self.horizontalLayout.addWidget(self.button_connect)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setStyleSheet("QTextBrowser {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 10px;                       \n"
"    border: 2px solid rgb(0, 150, 214);   \n"
"    color: rgb(0, 0, 0);                \n"
"}\n"
"\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_message = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(10)
        self.line_message.setFont(font)
        self.line_message.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"")
        self.line_message.setObjectName("line_message")
        self.horizontalLayout_2.addWidget(self.line_message)
        self.button_send = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_send.setFont(font)
        self.button_send.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 10px;                        \n"
"    color: rgb(0, 150, 214);            \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(227, 24, 55);           \n"
"}\n"
"")
        self.button_send.setObjectName("button_send")
        self.horizontalLayout_2.addWidget(self.button_send)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.line_ip.setText(_translate("MainWindow", "IP:"))
        self.label_status.setText(_translate("MainWindow", "Статус: не подключён"))
        self.button_connect.setText(_translate("MainWindow", "Подключиться"))
        self.button_send.setText(_translate("MainWindow", "Отправить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
