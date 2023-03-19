# booking info

from PyQt5 import QtCore, QtWidgets
from config import X, Y
from table_view import TablePage
import sys
import datetime


class BookingInfoPage(object):
    def __init__(self, userID) -> None:
        self.Dialog = QtWidgets.QDialog()
        self.userID = userID
        self.setupUI()
        self.Dialog.show()
        self.Dialog.exec()

    def setupUI(self):
        self.x = X // 3
        self.y = Y

        self.Dialog.resize(self.x, self.y)
        self.Dialog.setWindowTitle("Booking")
        self.Dialog.setStyleSheet("font-family: Comic Sans MS;")

        self.calender = QtWidgets.QCalendarWidget(self.Dialog)
        self.calender.setFixedSize(self.x, self.y // 2)
        self.calender.setMinimumDate(datetime.date.today())

        self.numberOfPeople = QtWidgets.QLineEdit(self.Dialog)
        self.numberOfPeople.setFixedSize(self.x, self.y // 8)
        self.numberOfPeople.setAlignment(QtCore.Qt.AlignCenter)
        self.numberOfPeople.move(0, self.y * 5 // 8)
        self.numberOfPeople.setPlaceholderText("Number Of People")

        self.selectTime = QtWidgets.QTimeEdit(self.Dialog)
        self.selectTime.setFixedSize(self.x, self.y // 8)
        self.selectTime.setAlignment(QtCore.Qt.AlignCenter)
        self.selectTime.move(0, self.y // 2)
        self.selectTime.setMaximumTime(datetime.time(hour=20))
        self.selectTime.setMinimumTime(datetime.time(hour=12))

        self.selectTable = QtWidgets.QPushButton(self.Dialog)
        self.selectTable.setFixedSize(self.x, self.y // 4)
        self.selectTable.move(0, self.y * 3 // 4)
        self.selectTable.setText("Select Table")
        self.selectTable.clicked.connect(self.select_table)

    def select_table(self):
        try:
            if int(self.numberOfPeople.text()) < 7:
                self.Dialog.close()
                TablePage(
                    self.calender.selectedDate(),
                    self.selectTime.time(),
                    int(self.numberOfPeople.text()),
                    self.userID,
                )
        except:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = BookingInfoPage(7)
