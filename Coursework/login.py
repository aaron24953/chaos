from PyQt5 import QtCore, QtWidgets
from random import random
import config
import sys

class ExamplePage(object):
    def __init__(self) -> None:
        Dialog=QtWidgets.QDialog()
        self.setupUI(Dialog)
        Dialog.show()
        Dialog.exec()

    def setupUI(self, Dialog):
        self.x=config.X/2
        self.y=config.Y
        Dialog.resize(self.x, self.y)
        Dialog.setWindowTitle("login")
        self.pushButton=QtWidgets.QPushButton(Dialog)
        self.pushButton.setFixedSize(self.x/3, self.y/3)
        self.pushButton.setText("example PB")
        self.pushButton.move(self.x/3, self.y/3)
        self.pushButton.clicked.connect(self.randomisePB)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = ExamplePage()
