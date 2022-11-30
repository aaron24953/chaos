# account page

# view bookings and general account info

from PyQt5 import QtCore, QtWidgets
from config import X, Y
import sys
from dbCon import dbCon


class AccountViewPage(object):
    def __init__(self, userID) -> None:
        Dialog = QtWidgets.QDialog()

        self.cnxn = dbCon()
        self.cursor = self.cnxn.cursor()
        self.cursor.execute(f"select * from Customer where CustomerID = {userID}")

        self.userInfo = self.cursor.fetchone()

        self.setupUI(Dialog)
        Dialog.show()
        Dialog.exec()

    def setupUI(self, Dialog):
        self.x = X // 3
        self.y = Y

        Dialog.resize(self.x, self.y)
        Dialog.setWindowTitle("My Account")
        Dialog.setStyleSheet("font-family: Comic Sans MS;")

        self.nameDisplay = QtWidgets.QLabel(Dialog)
        self.nameDisplay.setFixedSize(self.x, self.y // 6)
        self.nameDisplay.setAlignment(QtCore.Qt.AlignHCenter)
        self.nameDisplay.setText(
            f"Name: {self.userInfo[3]} {self.userInfo[4]}\nUsername: {self.userInfo[1]}"
        )

        self.createBookingButton = QtWidgets.QPushButton(Dialog)
        self.createBookingButton.clicked.connect(self.create_booking)
        self.createBookingButton.setText("Create Booking")
        self.createBookingButton.setFixedSize(self.x, self.y // 12)
        self.createBookingButton.move(0, self.y // 12)

        self.bookingsDisplay = QtWidgets.QTableWidget(Dialog)
        self.bookingsDisplay.setFixedSize(self.x, self.y * 5 // 6)
        self.bookingsDisplay.move(0, self.y // 6)
        self.bookingsDisplay.setColumnCount(4)
        columnNames = ["Date", "Time", "Table", "Number of People"]
        columnProportions = [20, 15, 20, 35]
        self.bookingsDisplay.setHorizontalHeaderLabels(columnNames)
        for i in range(len(columnNames)):
            self.bookingsDisplay.setColumnWidth(i, columnProportions[i] * self.x // 100)

        self.cursor.execute(
            f"select Time, TableID, numberOfPeople from Booking where CustomerID = {self.userInfo[0]}"
        )
        self.bookings = self.cursor.fetchall()
        self.bookingsDisplay.setRowCount(len(self.bookings))
        for i in range(len(self.bookings)):
            date = str(self.bookings[i][0])[:10]
            time = str(self.bookings[i][0])[-8:-3]
            date = f"{date[-2:]}/{date[-5:-3]}/{date[2:4]}"
            self.bookingsDisplay.setItem(i, 0, QtWidgets.QTableWidgetItem(date))
            self.bookingsDisplay.setItem(i, 1, QtWidgets.QTableWidgetItem(time))
            for j in range(1, len(self.bookings[i])):
                self.bookingsDisplay.setItem(
                    i, j + 1, QtWidgets.QTableWidgetItem(str(self.bookings[i][j]))
                )

        # add membership status later

    def create_booking(self):
        from booking_info import BookingInfoPage
        BookingInfoPage(self.userInfo[0])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = AccountViewPage(7)
