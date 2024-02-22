from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QFont
import sys
import cv2


class InitialWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("教師資格考試測驗系統")
        self.setWindowIcon(QtGui.QIcon("./windowsicon.ico"))

        # 初始螢幕視窗大小(固定)
        self.setFixedSize(1200, 768)

        # ----- 參數設定 -----
        self.init_title = QtWidgets.QLabel(self)

        # 調整視窗大小按鈕變數
        self.winsize_group = QtWidgets.QButtonGroup(self)
        self.small = QtWidgets.QRadioButton(self)
        self.median = QtWidgets.QRadioButton(self)
        self.large = QtWidgets.QRadioButton(self)
        self.label_size = QtWidgets.QLabel(self)
        # -----

        self._windows_setting()
        self.ui()

    def _windows_setting(self):
        # 讓視窗在螢幕正中間顯示
        screen = QtWidgets.QApplication.desktop()
        screen_width, screen_height = screen.width(), screen.height()
        width, height = self.width(), self.height()
        self.move((screen_width - width) // 2, (screen_height - height) // 2)

        # 利用視窗大小, 計算每個元件的相對位置 & 設定 CSS 樣式
        # 1. 初始畫面標題
        init_title_h = int(height // 4)
        self.init_title.setGeometry(0, 0, width, init_title_h)

        self.init_title.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignJustify)
        self.init_title.setFont(QFont('標楷體'))
        self.init_title.setStyleSheet(
            '''
            color: black;
            font-size: 76px;
            font-weight: bold;
            border: solid black;
            border-width: 0px 0px 2px 0px;
            '''
        )

        # 2. 調整螢幕尺寸大小的按鈕 & 標籤
        start_x = int(self.width() * 0.05)
        start_y = int(self.height() * 0.8)
        group_w = int(self.width() // 2) - start_x
        group_h = int(self.height() - start_y) // 5

        self.label_size.setGeometry(int(start_x // 2), start_y, group_w, group_h)
        self.small.setGeometry(start_x, start_y + group_h, group_w, group_h)
        self.median.setGeometry(start_x, start_y + group_h * 2, group_w, group_h)
        self.large.setGeometry(start_x, start_y + group_h * 3, group_w, group_h)

        self.label_size.setFont(QFont('DFkai-sb', 18))
        self.small.setFont(QFont('Times New Roman', 14))
        self.median.setFont(QFont('Times New Roman', 14))
        self.large.setFont(QFont('Times New Roman', 14))

    def ui(self):
        # 設定初始畫面的標題
        self.init_title.setText('教  檢  測  驗  系  統')

        # windows size select
        self.label_size.setText('選擇視窗大小：')
        self.small.setChecked(True)
        self.small.setText('1200x768')
        self.median.setText('1600x900')
        self.large.setText('1920x1080')

        self.winsize_group.addButton(self.small, id=1)
        self.winsize_group.addButton(self.median, id=2)
        self.winsize_group.addButton(self.large, id=3)

        self.winsize_group.buttonClicked.connect(self._win_select_event)
        pass

    def _win_select_event(self):
        select_id = self.winsize_group.checkedId()
        if select_id == 1:
            self.setFixedSize(1280, 800)
        elif select_id == 2:
            self.setFixedSize(1600, 900)
        elif select_id == 3:
            self.setFixedSize(1920, 1080)

        self._windows_setting()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = InitialWindow()
    window.show()
    sys.exit(app.exec_())
