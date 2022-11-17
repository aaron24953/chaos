from PyQt5 import QtCore, QtWidgets
from random import random
import sys

class ExamplePage(object):
    def __init__(self) -> None:
        Dialog=QtWidgets.QDialog()
        self.setupUI(Dialog)
        Dialog.show()
        Dialog.exec()

    def setupUI(self, Dialog):
        self.x=600
        self.y=600
        Dialog.resize(self.x, self.y)
        Dialog.setWindowTitle("example")
        self.pushButton=QtWidgets.QPushButton(Dialog)
        self.pushButton.setFixedSize(self.x/3, self.y/3)
        self.pushButton.setText("example PB")
        self.pushButton.move(self.x/3, self.y/3)
        self.pushButton.clicked.connect(self.randomisePB)

    def randomisePB(self):
        self.pushButton.move(self.x*2/3*random(), self.y*2/3*random())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = ExamplePage()
