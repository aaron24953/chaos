# booking_confirm_page

from PyQt5 import QtCore, QtWidgets
from config import X, Y
import sys


class BookingConfirmPage(object):
    def __init__(self, dateTime, numberOfPeople, table) -> None:
        self.dateTime = dateTime
        self.numberOfPeople = numberOfPeople
        self.table = table
        Dialog = QtWidgets.QDialog()
        self.setupUI(Dialog)
        Dialog.show()
        Dialog.exec()

    def setupUI(self, Dialog: QtWidgets.QDialog):
        self.x = X // 6
        self.y = Y // 4
        Dialog.resize(self.x, self.y)
        Dialog.setWindowTitle("Confirm Booking")
        Dialog.setStyleSheet("font-family: Comic Sans MS;")

        self.numberOfPeopleDisplay = QtWidgets.QLabel(Dialog)
        self.numberOfPeopleDisplay.setFixedSize(self.x, self.y // 5)
        self.numberOfPeopleDisplay.move(0, self.y // 5)
        self.numberOfPeopleDisplay.setText(f"Number Of People: {self.numberOfPeople}")

        self.dateTimeDisplay = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeDisplay.setFixedSize(self.x, self.y // 5)
        self.dateTimeDisplay.setDateTime(self.dateTime)
        self.dateTimeDisplay.setReadOnly(True)

        self.tableDisplay = QtWidgets.QLabel(Dialog)
        self.tableDisplay.setFixedSize(self.x, self.y // 5)
        self.tableDisplay.move(0, self.y * 2 // 5)
        self.tableDisplay.setText(f"Table: {self.table}")

        self.confirmButton = QtWidgets.QPushButton(Dialog)
        self.confirmButton.setFixedSize(self.x, self.y * 2 // 5)
        self.confirmButton.move(0, self.y * 3 // 5)
        self.confirmButton.setText("Confirm Booking")
        self.confirmButton.clicked.connect(self.confirm)

    def confirm(self):
        # add booking to database
        # open an account view page
        MainPage()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = BookingConfirmPage(2022, 11, 28, 14, 30, 6, 3)
