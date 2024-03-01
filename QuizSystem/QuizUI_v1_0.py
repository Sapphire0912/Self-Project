from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QFont, QPixmap, QPalette, QColor
from json import load, dump
from datetime import datetime
import os
import sys


class WindowSetting(QtWidgets.QWidget):
    """
    WindowSetting: 處理視窗基本參數
    """
    def __init__(self):
        super(WindowSetting, self).__init__()

        self.window_width = self.width()
        self.window_height = self.height()

    def windows_format(self):
        self.setWindowTitle("教師資格考試測驗系統")
        self.setWindowIcon(QtGui.QIcon("./image/windowsicon.ico"))
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.setFixedSize(self.window_width, self.window_height)


class InitialWindow(WindowSetting):
    def __init__(self):
        super(InitialWindow, self).__init__()

        self.window_width = 900
        self.window_height = 900
        self.windows_format()
        print(self.width(), self.height())



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = InitialWindow()
    window.show()
    sys.exit(app.exec_())
