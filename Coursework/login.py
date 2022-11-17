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
        self.x=config.X/3
        self.y=config.Y/2
        Dialog.resize(self.x, self.y)
        Dialog.setWindowTitle("Login")

        self.pushButton=QtWidgets.QPushButton(Dialog)
        self.pushButton.setFixedSize(self.x/3, self.y/6)
        self.pushButton.setText("Login")
        self.pushButton.move(self.x/3, self.y*5/6)
        #  self.pushButton.clicked.connect(self.randomisePB)

        self.loginText = QtWidgets.QLabel(Dialog)
        self.loginText.setText("Please Log In")
        self.loginText.setAlignment(QtCore.Qt.AlignCenter)
        self.loginText.resize(self.x/5, self.y/5)
        self.loginText.move(self.x*2/5, 0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = ExamplePage()
