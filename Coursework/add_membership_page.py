# add_membership_page
from PyQt5 import QtCore, QtWidgets
import sys
from dbCon import dbCon
from config import X, Y


class AddMembershipPage(object):
    def __init__(self) -> None:
        Dialog = QtWidgets.QDialog()
        self.setupUI(Dialog)
        Dialog.show()
        Dialog.exec()

    def setupUI(self, Dialog: QtWidgets.QDialog):
        self.x = X * 2 // 3
        self.y = Y
        Dialog.resize(self.x, self.y)
        Dialog.setWindowTitle("Main Menu")
        Dialog.setStyleSheet("font-family: Comic Sans MS;")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = AddMembershipPage()
