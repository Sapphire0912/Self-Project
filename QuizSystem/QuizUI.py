from PyQt5 import QtWidgets, QtCore, QtGui
import sys


class InitialWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("教師資格考試測驗系統")
        self.setWindowIcon(QtGui.QIcon("./windowsicon.ico"))
        pass
