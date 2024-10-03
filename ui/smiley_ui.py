from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 255)
        MainWindow.setStyleSheet("background-color: rgb(0, 103, 177);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 368, 238))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.laughter = QtWidgets.QPushButton(self.layoutWidget)
        self.laughter.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.laughter.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/smiley/laughter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.laughter.setIcon(icon)
        self.laughter.setIconSize(QtCore.QSize(40, 40))
        self.laughter.setObjectName("laughter")
        self.horizontalLayout_3.addWidget(self.laughter)
        self.swearing = QtWidgets.QPushButton(self.layoutWidget)
        self.swearing.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.swearing.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/smiley/swearing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.swearing.setIcon(icon1)
        self.swearing.setIconSize(QtCore.QSize(40, 40))
        self.swearing.setObjectName("swearing")
        self.horizontalLayout_3.addWidget(self.swearing)
        self.astonished = QtWidgets.QPushButton(self.layoutWidget)
        self.astonished.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.astonished.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/smiley/astonished.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.astonished.setIcon(icon2)
        self.astonished.setIconSize(QtCore.QSize(40, 40))
        self.astonished.setObjectName("astonished")
        self.horizontalLayout_3.addWidget(self.astonished)
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_16.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.pushButton_16.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/smiley/angry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon3)
        self.pushButton_16.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_3.addWidget(self.pushButton_16)
        self.sleep = QtWidgets.QPushButton(self.layoutWidget)
        self.sleep.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.sleep.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/smiley/sleep.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sleep.setIcon(icon4)
        self.sleep.setIconSize(QtCore.QSize(40, 40))
        self.sleep.setObjectName("sleep")
        self.horizontalLayout_3.addWidget(self.sleep)
        self.angry_demon = QtWidgets.QPushButton(self.layoutWidget)
        self.angry_demon.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.angry_demon.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/smiley/angry_demon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.angry_demon.setIcon(icon5)
        self.angry_demon.setIconSize(QtCore.QSize(40, 40))
        self.angry_demon.setObjectName("angry_demon")
        self.horizontalLayout_3.addWidget(self.angry_demon)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.thumbs_up = QtWidgets.QPushButton(self.layoutWidget)
        self.thumbs_up.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.thumbs_up.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/smiley/thumbs_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.thumbs_up.setIcon(icon6)
        self.thumbs_up.setIconSize(QtCore.QSize(40, 40))
        self.thumbs_up.setObjectName("thumbs_up")
        self.horizontalLayout.addWidget(self.thumbs_up)
        self.thumbs_down = QtWidgets.QPushButton(self.layoutWidget)
        self.thumbs_down.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.thumbs_down.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("image/smiley/thumbs_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.thumbs_down.setIcon(icon7)
        self.thumbs_down.setIconSize(QtCore.QSize(40, 40))
        self.thumbs_down.setObjectName("thumbs_down")
        self.horizontalLayout.addWidget(self.thumbs_down)
        self.waving = QtWidgets.QPushButton(self.layoutWidget)
        self.waving.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.waving.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("image/smiley/waving.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.waving.setIcon(icon8)
        self.waving.setIconSize(QtCore.QSize(40, 40))
        self.waving.setObjectName("waving")
        self.horizontalLayout.addWidget(self.waving)
        self.victory = QtWidgets.QPushButton(self.layoutWidget)
        self.victory.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.victory.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("image/smiley/victory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.victory.setIcon(icon9)
        self.victory.setIconSize(QtCore.QSize(40, 40))
        self.victory.setObjectName("victory")
        self.horizontalLayout.addWidget(self.victory)
        self.fuck = QtWidgets.QPushButton(self.layoutWidget)
        self.fuck.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.fuck.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("image/smiley/fuck.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fuck.setIcon(icon10)
        self.fuck.setIconSize(QtCore.QSize(40, 40))
        self.fuck.setObjectName("fuck")
        self.horizontalLayout.addWidget(self.fuck)
        self.oncoming = QtWidgets.QPushButton(self.layoutWidget)
        self.oncoming.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.oncoming.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("image/smiley/oncoming.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oncoming.setIcon(icon11)
        self.oncoming.setIconSize(QtCore.QSize(40, 40))
        self.oncoming.setObjectName("oncoming")
        self.horizontalLayout.addWidget(self.oncoming)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.eyes = QtWidgets.QPushButton(self.layoutWidget)
        self.eyes.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.eyes.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("image/smiley/eyes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eyes.setIcon(icon12)
        self.eyes.setIconSize(QtCore.QSize(40, 40))
        self.eyes.setObjectName("eyes")
        self.horizontalLayout_4.addWidget(self.eyes)
        self.moai = QtWidgets.QPushButton(self.layoutWidget)
        self.moai.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.moai.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("image/smiley/moai.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moai.setIcon(icon13)
        self.moai.setIconSize(QtCore.QSize(40, 40))
        self.moai.setObjectName("moai")
        self.horizontalLayout_4.addWidget(self.moai)
        self.monkey = QtWidgets.QPushButton(self.layoutWidget)
        self.monkey.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.monkey.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("image/smiley/monkey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.monkey.setIcon(icon14)
        self.monkey.setIconSize(QtCore.QSize(40, 40))
        self.monkey.setObjectName("monkey")
        self.horizontalLayout_4.addWidget(self.monkey)
        self.monster = QtWidgets.QPushButton(self.layoutWidget)
        self.monster.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.monster.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("image/smiley/monster.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.monster.setIcon(icon15)
        self.monster.setIconSize(QtCore.QSize(40, 40))
        self.monster.setObjectName("monster")
        self.horizontalLayout_4.addWidget(self.monster)
        self.poo = QtWidgets.QPushButton(self.layoutWidget)
        self.poo.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.poo.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("image/smiley/poo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.poo.setIcon(icon16)
        self.poo.setIconSize(QtCore.QSize(40, 40))
        self.poo.setObjectName("poo")
        self.horizontalLayout_4.addWidget(self.poo)
        self.ogre = QtWidgets.QPushButton(self.layoutWidget)
        self.ogre.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.ogre.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("image/smiley/ogre.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ogre.setIcon(icon17)
        self.ogre.setIconSize(QtCore.QSize(40, 40))
        self.ogre.setObjectName("ogre")
        self.horizontalLayout_4.addWidget(self.ogre)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.heart = QtWidgets.QPushButton(self.layoutWidget)
        self.heart.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.heart.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("image/smiley/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.heart.setIcon(icon18)
        self.heart.setIconSize(QtCore.QSize(40, 40))
        self.heart.setObjectName("heart")
        self.horizontalLayout_5.addWidget(self.heart)
        self.nail_polish = QtWidgets.QPushButton(self.layoutWidget)
        self.nail_polish.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.nail_polish.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("image/smiley/nail_polish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nail_polish.setIcon(icon19)
        self.nail_polish.setIconSize(QtCore.QSize(40, 40))
        self.nail_polish.setObjectName("nail_polish")
        self.horizontalLayout_5.addWidget(self.nail_polish)
        self.ninja = QtWidgets.QPushButton(self.layoutWidget)
        self.ninja.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.ninja.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("image/smiley/ninja.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ninja.setIcon(icon20)
        self.ninja.setIconSize(QtCore.QSize(40, 40))
        self.ninja.setObjectName("ninja")
        self.horizontalLayout_5.addWidget(self.ninja)
        self.woman_dancing = QtWidgets.QPushButton(self.layoutWidget)
        self.woman_dancing.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.woman_dancing.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("image/smiley/woman_dancing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.woman_dancing.setIcon(icon21)
        self.woman_dancing.setIconSize(QtCore.QSize(40, 40))
        self.woman_dancing.setObjectName("woman_dancing")
        self.horizontalLayout_5.addWidget(self.woman_dancing)
        self.woman_shrugging = QtWidgets.QPushButton(self.layoutWidget)
        self.woman_shrugging.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.woman_shrugging.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("image/smiley/woman_shrugging.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.woman_shrugging.setIcon(icon22)
        self.woman_shrugging.setIconSize(QtCore.QSize(40, 40))
        self.woman_shrugging.setObjectName("woman_shrugging")
        self.horizontalLayout_5.addWidget(self.woman_shrugging)
        self.skull = QtWidgets.QPushButton(self.layoutWidget)
        self.skull.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius: 15px;                 \n"
"    padding: 5px;                        \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}")
        self.skull.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("image/smiley/skull.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.skull.setIcon(icon23)
        self.skull.setIconSize(QtCore.QSize(40, 40))
        self.skull.setObjectName("skull")
        self.horizontalLayout_5.addWidget(self.skull)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
