# add_membership_page
from PyQt5 import QtCore, QtWidgets
import sys
from dbCon import dbCon
from config import X, Y


class AddMembershipPage(object):
    def __init__(self) -> None:
        self.Dialog = QtWidgets.QDialog()
        self.setupUI()
        self.cnxn = dbCon()
        self.cursor = self.cnxn.cursor()
        self.Dialog.show()
        self.Dialog.exec()

    def setupUI(self):
        self.x = X // 4
        self.y = Y // 2
        self.Dialog.resize(self.x, self.y)
        self.Dialog.setWindowTitle("Add Membership")
        self.Dialog.setStyleSheet("font-family: Comic Sans MS;")

        self.customerIDBox = QtWidgets.QLineEdit(self.Dialog)
        self.customerIDBox.setFixedSize(self.x, self.y // 4)
        self.customerIDBox.setPlaceholderText("CustomerID")

        self.startDateBox = QtWidgets.QLineEdit(self.Dialog)
        self.startDateBox.setFixedSize(self.x, self.y // 4)
        self.startDateBox.setPlaceholderText("Start Date (yyyy-mm-dd)")
        self.startDateBox.move(0, self.y // 4)

        self.endDateBox = QtWidgets.QLineEdit(self.Dialog)
        self.endDateBox.setFixedSize(self.x, self.y // 4)
        self.endDateBox.setPlaceholderText("End Date (yyyy-mm-dd)")
        self.endDateBox.move(0, self.y * 2 // 4)

        self.confirmButton = QtWidgets.QPushButton(self.Dialog)
        self.confirmButton.setText("Confirm")
        self.confirmButton.setFixedSize(self.x, self.y // 4)
        self.confirmButton.move(0, self.y * 3 // 4)
        self.confirmButton.clicked.connect(self.add_membership)

    def add_membership(self):
        self.cursor.execute("select max(MembershipID) from Membership")
        membershipID = self.cursor.fetchone()[0] + 1
        self.cursor.execute(f"insert into Membership values ({membershipID}, {self.customerIDBox.text()}, '{self.startDateBox.text()}', '{self.endDateBox.text()}')")
        self.cursor.commit()
        self.Dialog.close()
        from staff_main_page import StaffMainPage
        StaffMainPage(2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = AddMembershipPage()