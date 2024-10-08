from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
        Dialog.setWindowIcon(QIcon('image/icon_log.png'))
        Dialog.setStyleSheet("background-color: rgb(0, 103, 177);")

        self.line_nickname = QtWidgets.QLineEdit(Dialog)
        self.line_nickname.setGeometry(QtCore.QRect(25, 80, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(12)
        self.line_nickname.setFont(font)
        self.line_nickname.setStyleSheet("QLineEdit {\n"
                                         "    background-color: rgb(255, 255, 255); \n"
                                         "    border-radius: 15px;                 \n"
                                         "    padding: 5px;                        \n"
                                         "}\n"
                                         "")
        self.line_nickname.setObjectName("line_nickname")

        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setGeometry(QtCore.QRect(120, 135, 65, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_ok.setFont(font)
        self.button_ok.setStyleSheet("QPushButton {\n"
                                     "    background-color: rgb(255, 255, 255); \n"
                                     "    border-radius: 15px;                 \n"
                                     "    padding: 5px;                        \n"
                                     "    color: rgb(0, 150, 214);       \n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    color: rgb(227, 24, 55);          \n"
                                     "}\n"
                                     "")
        self.button_ok.setObjectName("button_ok")

        self.label_nickname = QtWidgets.QLabel(Dialog)
        self.label_nickname.setGeometry(QtCore.QRect(48, 40, 204, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(14)
        self.label_nickname.setFont(font)
        self.label_nickname.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_nickname.setObjectName("label_nickname")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вход"))
        self.button_ok.setText(_translate("Dialog", "Ок"))
        self.label_nickname.setText(_translate("Dialog", "Введите ваш никнейм:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
