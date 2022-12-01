# staff_booking_confirm_page

from PyQt5 import QtCore, QtWidgets
from config import X, Y
from dbCon import dbCon
from staff_main_page import *
import sys


class StaffBookingConfirmPage(object):
    def __init__(self, dateTime, numberOfPeople, table, customerID, customerName) -> None:
        self.customerName = customerName
        self.dateTime = dateTime
        self.numberOfPeople = numberOfPeople
        self.table = table
        self.customerID = customerID
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

        self.dateTimeDisplay = QtWidgets.QDateTimeEdit(self.Dialog)
        self.dateTimeDisplay.setFixedSize(self.x, self.y // 5)
        self.dateTimeDisplay.setDateTime(self.dateTime)
        self.dateTimeDisplay.setReadOnly(True)

        self.informationDisplay = QtWidgets.QLabel(self.Dialog)
        self.informationDisplay.setFixedSize(self.x, self.y * 2 // 5)
        self.informationDisplay.move(0, self.y // 5)
        self.informationDisplay.setText(f"Table: {self.table}\nCustomer ID: {self.customerID}\nNumber Of People: {self.numberOfPeople}")

        self.confirmButton = QtWidgets.QPushButton(self.Dialog)
        self.confirmButton.setFixedSize(self.x, self.y * 2 // 5)
        self.confirmButton.move(0, self.y * 3 // 5)
        self.confirmButton.setText("Confirm Booking")
        self.confirmButton.clicked.connect(self.confirm)

        self.userIDDisplay = QtWidgets.QLabel(f"Customer ID: {self.customerID}")

    def confirm(self):

        self.cursor.execute("select max(BookingID) from Booking")
        bookingID = self.cursor.fetchone()[0] + 1
        self.dateTimeString = self.dateTime.toString("yyyy-MM-dd HH:mm:ss")
        if self.customerID != -1:
            self.cursor.execute(
                f"insert into Booking values ({bookingID},NULL,{self.customerID},{self.table},'{self.dateTimeString}',{self.numberOfPeople},NULL)"
            )
        else:
            self.cursor.execute(
                f"insert into Booking values ({bookingID},NULL,{self.customerID},{self.table},'{self.dateTimeString}',{self.numberOfPeople},'{self.customerName}')"
            )
        self.cursor.commit()

        self.Dialog.close()
        StaffMainPage(self.customerID)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = StaffBookingConfirmPage(QtCore.QDateTime.currentDateTime(), 6, 3, 7, "")
