# staff login page

from PyQt5 import QtCore, QtWidgets
from config import X, Y
import sys


class StaffLoginPage(object):
    def __init__(self) -> None:
        self.Dialog = QtWidgets.QDialog()
        self.setupUI()
        self.Dialog.show()
        self.Dialog.exec()

    def setupUI(self):
        self.x = X // 6
        self.y = Y // 4
        self.Dialog.resize(self.x, self.y)
        self.Dialog.setWindowTitle("Login")
        self.Dialog.setStyleSheet("font-family: Comic Sans MS;")

        self.loginText = QtWidgets.QLabel(self.Dialog)
        self.loginText.setText("Log In")
        self.loginText.setAlignment(QtCore.Qt.AlignCenter)
        self.loginText.resize(self.x, self.y * 3 // 9)
        self.loginText.move(0, 0)
        self.loginText.setStyleSheet(f"font-size: {self.y // 4}px")

        self.username = QtWidgets.QLineEdit(self.Dialog)
        self.username.setPlaceholderText("Username")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.resize(self.x, self.y // 4)
        self.username.move(0, self.y * 3 // 9)

        self.password = QtWidgets.QLineEdit(self.Dialog)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.resize(self.x, self.y // 4)
        self.password.move(0, self.y * 5 // 9)

        self.loginButton = QtWidgets.QPushButton(self.Dialog)
        self.loginButton.setFixedSize(self.x // 3, self.y * 2 // 9)
        self.loginButton.setText("Login")
        self.loginButton.move(self.x // 3, self.y * 7 // 9)
        self.loginButton.clicked.connect(self.book)

    def book(self):
        self.Dialog.close()
        from staff_main_page import StaffMainPage
        StaffMainPage(2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = StaffLoginPage()
