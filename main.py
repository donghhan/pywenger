import sys
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import *
from lib.Pywenger import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec()
