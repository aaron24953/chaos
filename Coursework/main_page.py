#  main page

from PyQt5 import QtCore, QtWidgets
from config import X, Y
from create_account import AccountCreatePage
from login_page import LoginPage
import sys


class MainPage(object):
    def __init__(self) -> None:
        self.Dialog = QtWidgets.QDialog()
        self.setupUI()
        self.Dialog.show()
        self.Dialog.exec()

    def setupUI(self):
        self.x = X // 3
        self.y = Y // 2
        self.Dialog.resize(self.x, self.y)
        self.Dialog.setWindowTitle("Main Menu")
        self.Dialog.setStyleSheet("font-family: Comic Sans MS;")

        self.createButton = QtWidgets.QPushButton(self.Dialog)
        self.createButton.setFixedSize(self.x, self.y // 2)
        self.createButton.move(0, self.y // 2)
        self.createButton.setText("New Account")
        self.createButton.clicked.connect(self.create_account)

        self.LoginButton = QtWidgets.QPushButton(self.Dialog)
        self.LoginButton.setFixedSize(self.x, self.y // 2)
        self.LoginButton.setText("Login")
        self.LoginButton.clicked.connect(self.login)

    def login(self):
        LoginPage()

    def create_account(self):
        AccountCreatePage()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainPage()
