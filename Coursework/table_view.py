# table view page page

from PyQt5 import QtCore, QtWidgets
from config import X, Y
from booking_confirm_page import BookingConfirmPage
import sys


class TablePage(object):
    def __init__(self, date, time, numberOfPeople, userID) -> None:
        self.dateTime = QtCore.QDateTime(date, time)
        self.numberOfPeople = numberOfPeople
        self.userID = userID
        Dialog = QtWidgets.QDialog()
        self.setupUI(Dialog)
        Dialog.show()
        Dialog.exec()

    def setupUI(self, Dialog):
        self.x = X
        self.y = Y

        Dialog.resize(self.x, self.y)
        Dialog.setWindowTitle("Tables")
        Dialog.setStyleSheet("font-family: Comic Sans MS;")

        self.tables = [QtWidgets.QPushButton(Dialog) for i in range(10)]

        for i in range(4):
            self.tables[i].setFixedSize(self.x // 6, self.y // 6)
            self.tables[i].move(
                self.x // 20 + i % 2 * self.x // 4,
                self.y // 4 + i // 2 * self.y // 3
            )
            self.tables[i].setText(f"Table {i+1}")

        for i in range(4, 10):
            self.tables[i].setFixedSize(self.x // 10, self.y // 7)
            self.tables[i].move(
                self.x // 2 + (i - 4) % 3 * self.x // 8,
                self.y // 3 + (i - 4) // 3 * self.y // 4,
            )
            self.tables[i].setText(f"Table {i+1}")

        ## i hate this but python is wierd and i cant find another way to do it
        self.tables[0].clicked.connect(lambda: self.bookTable(0+1))
        self.tables[1].clicked.connect(lambda: self.bookTable(1+1))
        self.tables[2].clicked.connect(lambda: self.bookTable(2+1))
        self.tables[3].clicked.connect(lambda: self.bookTable(3+1))
        self.tables[4].clicked.connect(lambda: self.bookTable(4+1))
        self.tables[5].clicked.connect(lambda: self.bookTable(5+1))
        self.tables[6].clicked.connect(lambda: self.bookTable(6+1))
        self.tables[7].clicked.connect(lambda: self.bookTable(7+1))
        self.tables[8].clicked.connect(lambda: self.bookTable(8+1))
        self.tables[9].clicked.connect(lambda: self.bookTable(9+1))

    def bookTable(self, index):
        print(index)
        BookingConfirmPage(self.dateTime, self.numberOfPeople, index, self.userID)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = TablePage(2022, 11, 28, 14, 30, 6)
