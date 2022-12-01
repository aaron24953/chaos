from PyQt5 import QtCore, QtWidgets
from config import X, Y
import sys
from dbCon import dbCon


class LoginPage(object):
    def __init__(self) -> None:
        self.Dialog = QtWidgets.QDialog()
        self.setupUI()
        self.cnxn = dbCon()
        self.cursor = self.cnxn.cursor()
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

        self.invalidAcknowledgeButton = QtWidgets.QPushButton(self.Dialog)
        self.invalidAcknowledgeButton.setFixedSize(self.x, self.y // 2)
        self.invalidAcknowledgeButton.setText("Try Again")
        self.invalidAcknowledgeButton.clicked.connect(self.try_again)
        self.invalidAcknowledgeButton.hide()
        self.invalidAcknowledgeButton.move(0, self.y // 2)

        self.invalidLoginText = QtWidgets.QLabel(self.Dialog)
        self.invalidLoginText.setFixedSize(self.x, self.y // 2)
        self.invalidLoginText.hide()
        self.invalidLoginText.setText("Invalid Login")

    def book(self):
        self.cursor.execute(f"select CustomerID from customer where Username = '{self.username.text()}' and password = '{self.password.text()}'")
        user = self.cursor.fetchone()
        if user:
            self.Dialog.close()
            from account_page import AccountViewPage
            AccountViewPage(int(user[0]))
        else:
            self.invalid_login()

    def invalid_login(self):
        self.invalidAcknowledgeButton.show()
        self.invalidLoginText.show()
        self.loginText.hide()
        self.username.hide()
        self.password.hide()
        self.loginButton.hide()

    def try_again(self):
        self.invalidAcknowledgeButton.hide()
        self.invalidLoginText.hide()
        self.loginText.show()
        self.username.show()
        self.password.show()
        self.loginButton.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = LoginPage()
