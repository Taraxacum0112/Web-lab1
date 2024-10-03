from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 500)
        MainWindow.setStyleSheet("background-color: rgb(0, 103, 177);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 531, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_ip = QtWidgets.QLineEdit(self.layoutWidget)
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
        self.label_status = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_status.sizePolicy().hasHeightForWidth())
        self.label_status.setSizePolicy(sizePolicy)
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
        self.button_connect = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_connect.setFont(font)
        self.button_connect.setStyleSheet("QPushButton {\n"
"    background-color: rgb(227, 24, 55); \n"
"    border-radius: 10px;                 \n"
"    padding: 10px;                       \n"
"    color: rgb(255, 255, 255);              \n"
"    border: 2px solid rgb(227, 24, 55);    \n"
"    font-weight: bold;                    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 20, 50);        \n"
"    color: rgb(255, 255, 255);              \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 20, 45);      \n"
"    color: rgb(255, 255, 255);             \n"
"}\n"
"")
        self.button_connect.setObjectName("button_connect")
        self.horizontalLayout.addWidget(self.button_connect)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
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
        self.line_message = QtWidgets.QLineEdit(self.layoutWidget)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_clip = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_clip.sizePolicy().hasHeightForWidth())
        self.button_clip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_clip.setFont(font)
        self.button_clip.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 10px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"")
        self.button_clip.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icon_clip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_clip.setIcon(icon)
        self.button_clip.setIconSize(QtCore.QSize(25, 25))
        self.button_clip.setObjectName("button_clip")
        self.horizontalLayout_3.addWidget(self.button_clip)
        self.button_smiley = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_smiley.sizePolicy().hasHeightForWidth())
        self.button_smiley.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_smiley.setFont(font)
        self.button_smiley.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 10px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"")
        self.button_smiley.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/icon_smiley.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_smiley.setIcon(icon1)
        self.button_smiley.setIconSize(QtCore.QSize(25, 25))
        self.button_smiley.setObjectName("button_smiley")
        self.horizontalLayout_3.addWidget(self.button_smiley)
        self.button_send = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_send.sizePolicy().hasHeightForWidth())
        self.button_send.setSizePolicy(sizePolicy)
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
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"\n"
"")
        self.button_send.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/icon_send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_send.setIcon(icon2)
        self.button_send.setIconSize(QtCore.QSize(25, 25))
        self.button_send.setObjectName("button_send")
        self.horizontalLayout_3.addWidget(self.button_send)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
