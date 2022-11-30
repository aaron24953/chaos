# staff main page
# view bookings, memberships
from PyQt5 import QtCore, QtWidgets
import sys
from dbCon import dbCon
from config import X, Y


class StaffMainPage(object):
    def __init__(self, staffID) -> None:
        Dialog = QtWidgets.QDialog()
        self.cnxn = dbCon()
        self.staffID = staffID
        self.cursor = self.cnxn.cursor()
        self.setupUI(Dialog)
        Dialog.show()
        Dialog.exec()

    def setupUI(self, Dialog: QtWidgets.QDialog):
        self.x = X * 2 // 3
        self.y = Y
        Dialog.resize(self.x, self.y)
        Dialog.setWindowTitle("Main Menu")
        Dialog.setStyleSheet("font-family: Comic Sans MS;")

        self.bookingsDisplay = QtWidgets.QTableWidget(Dialog)
        self.bookingsDisplay.setFixedSize(self.x, self.y * 2 // 3)
        self.bookingsDisplay.move(0, self.y // 3)
        columnNames = [
            "Date",
            "Time",
            "BookingID",
            "Table",
            "Number of People",
            "CustomerID",
            "Name",
        ]
        self.bookingsDisplay.setColumnCount(len(columnNames))
        columnProportions = [14, 10, 12, 8, 20, 14, 19]
        self.bookingsDisplay.setHorizontalHeaderLabels(columnNames)
        for i in range(len(columnNames)):
            self.bookingsDisplay.setColumnWidth(i, columnProportions[i] * self.x // 100)

        self.cursor.execute(
            "select Time, BookingID, TableID, numberOfPeople, Customer.CustomerID, Firstname, Surname from Booking inner join Customer on Booking.CustomerID = Customer.CustomerID"
        )
        self.bookings = self.cursor.fetchall()
        self.bookingsDisplay.setRowCount(len(self.bookings))
        for i in range(len(self.bookings)):
            date = str(self.bookings[i][0])[:10]
            time = str(self.bookings[i][0])[-8:-3]
            date = f"{date[-2:]}/{date[-5:-3]}/{date[2:4]}"
            item = QtWidgets.QTableWidgetItem(date)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.bookingsDisplay.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem(time)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.bookingsDisplay.setItem(i, 1, item)
            for j in range(1, len(self.bookings[i]) - 2):
                item = QtWidgets.QTableWidgetItem(str(self.bookings[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.bookingsDisplay.setItem(i, j + 1, item)
            item = QtWidgets.QTableWidgetItem(
                str(self.bookings[i][j + 1]) + " " + str(self.bookings[i][j + 2])
            )
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.bookingsDisplay.setItem(i, j + 2, item)

        numIDBookings = len(self.bookings)
        self.cursor.execute(
            "select Time, BookingID, TableID, numberOfPeople, CustomerID, Name from Booking where CustomerID = -1"
        )
        self.bookings = self.cursor.fetchall()
        self.bookingsDisplay.setRowCount(numIDBookings + len(self.bookings))
        for i in range(len(self.bookings)):
            date = str(self.bookings[i][0])[:10]
            time = str(self.bookings[i][0])[-8:-3]
            date = f"{date[-2:]}/{date[-5:-3]}/{date[2:4]}"
            item = QtWidgets.QTableWidgetItem(date)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.bookingsDisplay.setItem(i + numIDBookings, 0, item)
            item = QtWidgets.QTableWidgetItem(time)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.bookingsDisplay.setItem(i + numIDBookings, 1, item)
            for j in range(1, len(self.bookings[i])):
                item = QtWidgets.QTableWidgetItem(str(self.bookings[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.bookingsDisplay.setItem(i + numIDBookings, j + 1, item)

        self.createBookingButton = QtWidgets.QPushButton(Dialog)
        self.createBookingButton.setFixedSize(self.x // 2, self.y // 3)
        self.createBookingButton.move(self.x // 2, 0)
        self.createBookingButton.setText("Create Booking")
        self.createBookingButton.clicked.connect(self.create_booking)

        self.addMembershipButton = QtWidgets.QPushButton(Dialog)
        self.addMembershipButton.setFixedSize(self.x // 2, self.y // 3)
        self.addMembershipButton.setText("Add Membership")
        self.addMembershipButton.clicked.connect(self.add_membership)

    def create_booking(self):
        from staff_create_booking_page import StaffCreateBookingPage
        StaffCreateBookingPage(self.staffID)

    def add_membership(self):
        from add_membership_page import AddMembershipPage
        AddMembershipPage()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = StaffMainPage(2)
