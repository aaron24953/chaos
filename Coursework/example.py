from PyQt5 import QtCore, QtWidgets
from random import random
import sys


class ExamplePage(object):
    def __init__(self) -> None:
        Dialog = QtWidgets.QDialog()
        self.setupUI(Dialog)
        Dialog.show()
        Dialog.exec()

    def setupUI(self, Dialog):
        self.x = 600
        self.y = 600

        Dialog.resize(self.x, self.y)
        Dialog.setWindowTitle("example")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setFixedSize(self.x / 3, self.y / 3)
        self.pushButton.setText("example PB")
        self.pushButton.move(self.x / 3, self.y / 3)
        self.pushButton.clicked.connect(self.randomisePB)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText("sample text")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.resize(self.x / 5, self.y / 5)
        self.label.move(self.x * 3 / 5, self.y / 5)
        self.label.setStyleSheet("border: 1px solid black;")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setPlaceholderText("example lineEdit")
        self.lineEdit.move(self.x / 10, self.y / 10)

    def randomisePB(self):
        self.pushButton.move(self.x * 2 / 3 * random(), self.y * 2 / 3 * random())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = ExamplePage()
