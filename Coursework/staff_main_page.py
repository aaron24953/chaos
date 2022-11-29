# staff main page
# view bookings, memberships
from PyQt5 import QtCore, QtWidgets
import sys
from dbCon import dbCon
from config import X, Y


class MainPage(object):
    def __init__(self) -> None:
        Dialog = QtWidgets.QDialog()
        self.cnxn = dbCon()
        self.cursor = self.cnxn.cursor()
        self.setupUI(Dialog)
        Dialog.show()
        Dialog.exec()

    def setupUI(self, Dialog: QtWidgets.QDialog):
        self.x = X // 2
        self.y = Y // 2
        Dialog.resize(self.x, self.y)
        Dialog.setWindowTitle("Main Menu")
        Dialog.setStyleSheet("font-family: Comic Sans MS;")

        self.bookingsDisplay = QtWidgets.QTableWidget(Dialog)
        self.bookingsDisplay.setFixedSize(self.x, self.y * 2 // 3)
        self.bookingsDisplay.setColumnCount(4)
        columnNames = ["Date", "Time", "Booking", "Table", "Number of People"]
        columnProportions = [20, 15, 20, 35]
        self.bookingsDisplay.setHorizontalHeaderLabels(columnNames)
        for i in range(len(columnNames)):
            self.bookingsDisplay.setColumnWidth(i, columnProportions[i] * self.x // 100)

        self.cursor.execute("select Time, BookingID, TableID, numberOfPeople, Customer.CustomerID, Firstname, Surname from Booking inner join Customer on Booking.CustomerID = Customer.CustomerID")
        self.bookings = self.cursor.fetchall()
        self.bookingsDisplay.setRowCount(len(self.bookings))
        for i in range(len(self.bookings)):
            date = str(self.bookings[i][0])[:10]
            time = str(self.bookings[i][0])[-8:-3]
            date = f"{date[-2:]}/{date[-5:-3]}/{date[2:4]}"
            self.bookingsDisplay.setItem(i, 0, QtWidgets.QTableWidgetItem(date))
            self.bookingsDisplay.setItem(i, 1, QtWidgets.QTableWidgetItem(time))
            for j in range(1, len(self.bookings[i])):
                self.bookingsDisplay.setItem(i, j+1, QtWidgets.QTableWidgetItem(str(self.bookings[i][j])))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainPage()
