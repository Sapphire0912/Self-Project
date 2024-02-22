from PyQt5 import QtWidgets, QtCore, QtGui
import sys


class InitialWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("教師資格考試測驗系統")
        self.setWindowIcon(QtGui.QIcon("./windowsicon.ico"))

        # 初始螢幕視窗大小(固定)
        self.setFixedSize(1280, 800)

        self._windows_setting()
        self._parameter_setting()
        self.ui()

    def _windows_setting(self):
        # 讓視窗在螢幕正中間顯示
        screen = QtWidgets.QApplication.desktop()
        screen_width, screen_height = screen.width(), screen.height()
        width, height = self.width(), self.height()
        self.move((screen_width - width)//2, (screen_height - height) // 2)

    def _parameter_setting(self):
        self.btn_win_select_group = QtWidgets.QButtonGroup(self)
        self.label2 = QtWidgets.QLabel(self)


    def ui(self):
        # 設定初始畫面
        label = QtWidgets.QLabel(self)
        label.setText('教檢測驗系統')

        # unit test
        small = QtWidgets.QRadioButton(self)
        small.setGeometry(30, 30, 100, 20)
        small.setText('1280x800')

        median = QtWidgets.QRadioButton(self)
        median.setGeometry(30, 60, 100, 20)
        median.setText('1600x900')

        large = QtWidgets.QRadioButton(self)
        large.setGeometry(30, 90, 100, 20)
        large.setText('1920x1080')

        self.btn_win_select_group.addButton(small, id=1)
        self.btn_win_select_group.addButton(median, id=2)
        self.btn_win_select_group.addButton(large, id=3)

        self.btn_win_select_group.buttonClicked.connect(self._win_select_event)
        self.label2.setGeometry(30, 120, 100, 20)
        pass

    def _win_select_event(self):
        self.label2.setText(str(self.btn_win_select_group.checkedId()))
        sizeDict = {
            1: [1280, 800],
            2: [1600, 900],
            3: [1920, 1080]
        }
        self.setFixedSize(sizeDict[self.btn_win_select_group.checkedId()][0], sizeDict[self.btn_win_select_group.checkedId()][1])
        self._windows_setting()
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = InitialWindow()
    window.show()
    sys.exit(app.exec_())
