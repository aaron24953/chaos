# staff_create_booking_page

# booking info

from PyQt5 import QtCore, QtWidgets
from config import X, Y
import sys


class StaffCreateBookingPage(object):
    def __init__(self, userID) -> None:
        Dialog = QtWidgets.QDialog()
        self.bookByID = False
        self.userID = userID
        self.setupUI(Dialog)
        Dialog.show()
        Dialog.exec()

    def setupUI(self, Dialog):
        self.x = X // 3
        self.y = Y

        Dialog.resize(self.x, self.y)
        Dialog.setWindowTitle("Booking")
        Dialog.setStyleSheet("font-family: Comic Sans MS;")

        self.calender = QtWidgets.QCalendarWidget(Dialog)
        self.calender.setFixedSize(self.x, self.y // 2)

        self.numberOfPeople = QtWidgets.QLineEdit(Dialog)
        self.numberOfPeople.setFixedSize(self.x, self.y // 8)
        self.numberOfPeople.setAlignment(QtCore.Qt.AlignCenter)
        self.numberOfPeople.move(0, self.y * 5 // 8)
        self.numberOfPeople.setPlaceholderText("Number Of People")

        self.selectTime = QtWidgets.QTimeEdit(Dialog)
        self.selectTime.setFixedSize(self.x, self.y // 8)
        self.selectTime.setAlignment(QtCore.Qt.AlignCenter)
        self.selectTime.move(0, self.y // 2)

        self.selectTable = QtWidgets.QPushButton(Dialog)
        self.selectTable.setFixedSize(self.x, self.y // 8)
        self.selectTable.move(0, self.y * 7 // 8)
        self.selectTable.setText("Select Table")
        self.selectTable.clicked.connect(self.select_table)

        self.customerIDButton = QtWidgets.QPushButton(Dialog)
        self.customerIDButton.setFixedSize(self.x // 2, self.y // 8)
        self.customerIDButton.move(0, self.y * 3 // 4)
        self.customerIDButton.setText("Book by ID")
        self.customerIDButton.clicked.connect(self.book_by_id)

        self.customerNameButton = QtWidgets.QPushButton(Dialog)
        self.customerNameButton.setFixedSize(self.x // 2, self.y // 8)
        self.customerNameButton.move(self.x // 2, self.y * 3 // 4)
        self.customerNameButton.setText("Book by Name")
        self.customerNameButton.clicked.connect(self.book_by_name)

        self.customerFirstnameBox = QtWidgets.QLineEdit(Dialog)
        self.customerFirstnameBox.setFixedSize(self.x, self.y // 16)
        self.customerFirstnameBox.move(0, self.y * 3 // 4)
        self.customerFirstnameBox.setPlaceholderText("Firstname")
        self.customerFirstnameBox.hide()

        self.customerIDBox = QtWidgets.QLineEdit(Dialog)
        self.customerIDBox.setFixedSize(self.x, self.y // 8)
        self.customerIDBox.move(0, self.y * 3 // 4)
        self.customerIDBox.setPlaceholderText("Customer ID")
        self.customerIDBox.hide()

        self.customerSurnameBox = QtWidgets.QLineEdit(Dialog)
        self.customerSurnameBox.setFixedSize(self.x, self.y // 16)
        self.customerSurnameBox.move(0, self.y * 13 // 16)
        self.customerSurnameBox.setPlaceholderText("Surname")
        self.customerSurnameBox.hide()

    def book_by_name(self):
        self.bookByID = False
        self.customerSurnameBox.show()
        self.customerFirstnameBox.show()
        self.customerNameButton.hide()
        self.customerIDButton.hide()

    def book_by_id(self):
        self.bookByID = True
        self.customerIDBox.show()
        self.customerNameButton.hide()
        self.customerIDButton.hide()

    def select_table(self):
        from staff_table_view_page import StaffTableViewPage
        if self.bookByID:
            self.userID = int(self.customerIDBox.text())
        else:
            self.userID = -1
        StaffTableViewPage(
            self.calender.selectedDate(),
            self.selectTime.time(),
            int(self.numberOfPeople.text()),
            self.userID,
            self.customerFirstnameBox.text() + " " + self.customerSurnameBox.text()
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = StaffCreateBookingPage(7)
