from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 812)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 981, 701))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("meme.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.test = QtWidgets.QPushButton(self.centralwidget)
        self.test.setGeometry(QtCore.QRect(0, 700, 481, 71))
        self.test.setObjectName("test")
        self.meme = QtWidgets.QPushButton(self.centralwidget)
        self.meme.setGeometry(QtCore.QRect(480, 700, 501, 71))
        self.meme.setObjectName("meme")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.meme.clicked.connect(self.show_meme)
        self.test.clicked.connect(self.show_test)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.test.setText(_translate("MainWindow", "TEST"))
        self.meme.setText(_translate("MainWindow", "MEME"))

    def show_test(self):
        self.photo.setPixmap(QtGui.QPixmap("testimage.jpg"))

    def show_meme(self):
        self.photo.setPixmap(QtGui.QPixmap("meme.jpg"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
