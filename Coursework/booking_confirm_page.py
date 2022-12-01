# booking_confirm_page

from PyQt5 import QtCore, QtWidgets
from config import X, Y
from dbCon import dbCon
from account_page import AccountViewPage
import sys


class BookingConfirmPage(object):
    def __init__(self, dateTime, numberOfPeople, table, userID) -> None:
        self.dateTime = dateTime
        self.numberOfPeople = numberOfPeople
        self.table = table
        self.userID = userID
        self.cnxn = dbCon()
        self.cursor = self.cnxn.cursor()
        self.Dialog = QtWidgets.QDialog()
        self.setupUI()
        self.Dialog.show()
        self.Dialog.exec()

    def setupUI(self):
        self.x = X // 6
        self.y = Y // 4
        self.Dialog.resize(self.x, self.y)
        self.Dialog.setWindowTitle("Confirm Booking")
        self.Dialog.setStyleSheet("font-family: Comic Sans MS;")

        self.numberOfPeopleDisplay = QtWidgets.QLabel(self.Dialog)
        self.numberOfPeopleDisplay.setFixedSize(self.x, self.y // 5)
        self.numberOfPeopleDisplay.move(0, self.y // 5)
        self.numberOfPeopleDisplay.setText(f"Number Of People: {self.numberOfPeople}")

        self.dateTimeDisplay = QtWidgets.QDateTimeEdit(self.Dialog)
        self.dateTimeDisplay.setFixedSize(self.x, self.y // 5)
        self.dateTimeDisplay.setDateTime(self.dateTime)
        self.dateTimeDisplay.setReadOnly(True)

        self.tableDisplay = QtWidgets.QLabel(self.Dialog)
        self.tableDisplay.setFixedSize(self.x, self.y // 5)
        self.tableDisplay.move(0, self.y * 2 // 5)
        self.tableDisplay.setText(f"Table: {self.table}")

        self.confirmButton = QtWidgets.QPushButton(self.Dialog)
        self.confirmButton.setFixedSize(self.x, self.y * 2 // 5)
        self.confirmButton.move(0, self.y * 3 // 5)
        self.confirmButton.setText("Confirm Booking")
        self.confirmButton.clicked.connect(self.confirm)

    def confirm(self):
        # add booking to database
        # open an account view page
        # MainPage()

        self.cursor.execute("select max(BookingID) from Booking")
        bookingID = self.cursor.fetchone()[0]
        if bookingID:
            bookingID += 1
        else:
            bookingID = 0
        self.dateTime = self.dateTime.toString("yyyy-MM-dd HH:mm:ss")
        self.cursor.execute(
            f"insert into Booking values ({bookingID},NULL,{self.userID},{self.table},'{self.dateTime}',{self.numberOfPeople},NULL)"
        )
        self.cursor.commit()
        self.Dialog.close()
        AccountViewPage(self.userID)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = BookingConfirmPage(QtCore.QDateTime.currentDateTime(), 6, 3, 7)
