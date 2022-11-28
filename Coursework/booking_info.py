# booking info

from PyQt5 import QtCore, QtWidgets
from config import X, Y
from table_view import TablePage
import sys


class BookingInfoPage(object):
    def __init__(self) -> None:
        Dialog = QtWidgets.QDialog()
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
        self.selectTable.setFixedSize(self.x, self.y // 4)
        self.selectTable.move(0, self.y * 3 // 4)
        self.selectTable.setText("Select Table")
        self.selectTable.clicked.connect(self.select_table)

    def select_table(self):
        TablePage(self.calender.selectedDate(), self.selectTime.time(), int(self.numberOfPeople.text()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = BookingInfoPage()
