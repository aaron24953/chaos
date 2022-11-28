#  create account page

from PyQt5 import QtCore, QtWidgets
from config import X, Y
import sys
from dbCon import dbCon


class AccountCreatePage(object):
    def __init__(self) -> None:
        Dialog = QtWidgets.QDialog()
        self.setupUI(Dialog)
        Dialog.show()
        Dialog.exec()

    def setupUI(self, Dialog):
        self.x = X // 4
        self.y = Y // 2
        Dialog.resize(self.x, self.y)
        Dialog.setWindowTitle("Create Account")
        Dialog.setStyleSheet("font-family: Comic Sans MS;")

        self.confirm = QtWidgets.QPushButton(Dialog)
        self.confirm.setText("Confirm")
        self.confirm.resize(self.x, self.y // 7)
        self.confirm.move(0, self.y * 6 // 7)
        self.confirm.clicked.connect(self.create_account)

        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setPlaceholderText("Username")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.resize(self.x, self.y // 7)
        self.username.move(0, self.y * 0 // 7)

        self.firstname = QtWidgets.QLineEdit(Dialog)
        self.firstname.setPlaceholderText("Firstname")
        self.firstname.setAlignment(QtCore.Qt.AlignCenter)
        self.firstname.resize(self.x, self.y // 7)
        self.firstname.move(0, self.y * 1 // 7)

        self.surname = QtWidgets.QLineEdit(Dialog)
        self.surname.setPlaceholderText("Surname")
        self.surname.setAlignment(QtCore.Qt.AlignCenter)
        self.surname.resize(self.x, self.y // 7)
        self.surname.move(0, self.y * 2 // 7)

        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        self.password.setPlaceholderText("Password")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.resize(self.x, self.y // 7)
        self.password.move(0, self.y * 3 // 7)

        self.phone = QtWidgets.QLineEdit(Dialog)
        self.phone.setPlaceholderText("Phone")
        self.phone.setAlignment(QtCore.Qt.AlignCenter)
        self.phone.resize(self.x, self.y // 7)
        self.phone.move(0, self.y * 4 // 7)

        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setPlaceholderText("Email")
        self.email.setAlignment(QtCore.Qt.AlignCenter)
        self.email.resize(self.x, self.y // 7)
        self.email.move(0, self.y * 5 // 7)

    def create_account(self):
        username = self.username.text()
        firstname = self.firstname.text()
        surname = self.surname.text()
        password = self.password.text()
        phone = self.phone.text()
        email = self.email.text()
        # upload values to database
        # cnxn = dbCon()

        # go to account view page


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = AccountCreatePage()
