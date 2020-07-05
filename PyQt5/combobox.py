# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'now.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(101, 171)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.combo1 = QtWidgets.QComboBox(self.centralwidget)
        self.combo1.setGeometry(QtCore.QRect(0, 0, 51, 31))
        self.combo1.setObjectName("combo1")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo2 = QtWidgets.QComboBox(self.centralwidget)
        self.combo2.setGeometry(QtCore.QRect(50, 0, 51, 31))
        self.combo2.setObjectName("combo2")
        self.combo2.addItem("")
        self.combo2.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 90, 91, 31))
        self.label.setObjectName("label")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(0, 40, 101, 31))
        self.submit.setObjectName("submit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 101, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.submit.clicked.connect(self.calculate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def calculate(self):
        y = int(self.combo1.currentText())
        x = int(self.combo2.currentText())
        xor = (x and not y) or (not x and y)
        if xor == True:
            xor = 1
        else:
            xor = 0
        self.label.setText("result: " + str(xor))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combo1.setItemText(0, _translate("MainWindow", "0"))
        self.combo1.setItemText(1, _translate("MainWindow", "1"))
        self.combo2.setItemText(0, _translate("MainWindow", "0"))
        self.combo2.setItemText(1, _translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "Result:"))
        self.submit.setText(_translate("MainWindow", "SUBMIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
