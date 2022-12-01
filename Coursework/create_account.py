#  create account page

from PyQt5 import QtCore, QtWidgets
from config import X, Y
import sys
from dbCon import dbCon


class AccountCreatePage(object):
    def __init__(self) -> None:
        self.Dialog = QtWidgets.QDialog()
        self.setupUI()
        self.Dialog.show()
        self.Dialog.exec()

    def setupUI(self):
        self.x = X // 4
        self.y = Y // 2
        self.Dialog.resize(self.x, self.y)
        self.Dialog.setWindowTitle("Create Account")
        self.Dialog.setStyleSheet("font-family: Comic Sans MS;")

        self.confirm = QtWidgets.QPushButton(self.Dialog)
        self.confirm.setText("Confirm")
        self.confirm.resize(self.x, self.y // 7)
        self.confirm.move(0, self.y * 6 // 7)
        self.confirm.clicked.connect(self.create_account)

        self.username = QtWidgets.QLineEdit(self.Dialog)
        self.username.setPlaceholderText("Username")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.resize(self.x, self.y // 7)
        self.username.move(0, self.y * 0 // 7)

        self.firstname = QtWidgets.QLineEdit(self.Dialog)
        self.firstname.setPlaceholderText("Firstname")
        self.firstname.setAlignment(QtCore.Qt.AlignCenter)
        self.firstname.resize(self.x, self.y // 7)
        self.firstname.move(0, self.y * 1 // 7)

        self.surname = QtWidgets.QLineEdit(self.Dialog)
        self.surname.setPlaceholderText("Surname")
        self.surname.setAlignment(QtCore.Qt.AlignCenter)
        self.surname.resize(self.x, self.y // 7)
        self.surname.move(0, self.y * 2 // 7)

        self.password = QtWidgets.QLineEdit(self.Dialog)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        self.password.setPlaceholderText("Password")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.resize(self.x, self.y // 7)
        self.password.move(0, self.y * 3 // 7)

        self.phone = QtWidgets.QLineEdit(self.Dialog)
        self.phone.setPlaceholderText("Phone")
        self.phone.setAlignment(QtCore.Qt.AlignCenter)
        self.phone.resize(self.x, self.y // 7)
        self.phone.move(0, self.y * 4 // 7)

        self.email = QtWidgets.QLineEdit(self.Dialog)
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

        cnxn = dbCon()
        cursor = cnxn.cursor()
        cursor.execute("select MAX(CustomerID) from Customer")
        custID = cursor.fetchone()[0] + 1
        cursor.execute(
            f"insert into Customer values ('{custID}','{username}','{password}','{firstname}','{surname}','{phone}','{email}')"
        )
        cursor.commit()

        self.Dialog.close()
        from account_page import AccountViewPage
        AccountViewPage(custID)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = AccountCreatePage()