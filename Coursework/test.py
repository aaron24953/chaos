from PyQt5 import QtCore, QtWidgets
import sys

class PbPage(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.button=QtWidgets.QPushButton("PB")
        self.setCentralWidget(self.button)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    page = PbPage()
    page.resize(800, 600)
    page.show()

    sys.exit(app.exec())
