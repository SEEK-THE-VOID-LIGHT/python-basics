#GUI TEST
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Test Programm")
        
        self.label = QtWidgets.QLabel(self)
        self.label.setText("dis is label")
        self.label.move(50,50)
        
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        self.b1.move(100,100)
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        print("clicked")
        self.label.setText("you pressed da fukin button")
        self.update()
        
    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()