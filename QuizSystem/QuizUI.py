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
        self.setFixedSize(960, 720)

        # ----- 參數設定 -----
        self.init_title = QtWidgets.QLabel(self)

        # 調整視窗大小按鈕變數
        self.winsize_group = QtWidgets.QButtonGroup(self)
        self.small = QtWidgets.QRadioButton(self)
        self.median = QtWidgets.QRadioButton(self)
        self.large = QtWidgets.QRadioButton(self)
        self.label_size = QtWidgets.QLabel(self)

        # 設定輸入框的變數
        self.description = QtWidgets.QTextEdit(self)

        # 設定測驗科目的標籤
        self.subject_title = QtWidgets.QLabel(self)
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
        group_w = int(self.width() // 4) - start_x
        group_h = int(self.height() - start_y) // 5

        self.label_size.setGeometry(int(start_x // 2), start_y, group_w, group_h)
        self.small.setGeometry(start_x, start_y + group_h, group_w, group_h)
        self.median.setGeometry(start_x, start_y + group_h * 2, group_w, group_h)
        self.large.setGeometry(start_x, start_y + group_h * 3, group_w, group_h)
        self.label_size.setStyleSheet('''
            border: solid black;
            border-width: 3px 3px 3px 3px;
        ''')

        self.label_size.setFont(QFont('DFkai-sb', 18))
        self.small.setFont(QFont('Times New Roman', 14))
        self.median.setFont(QFont('Times New Roman', 14))
        self.large.setFont(QFont('Times New Roman', 14))

        # 3. 設定輸入框的大小和位置
        desc_y = init_title_h + 20  # 在標題底下的 20 px
        desc_w = int(self.width() // 2) - start_x  # 和 btn group 對齊
        desc_h = int(self.height() * 2 // 4)
        self.description.setGeometry(int(start_x // 2), desc_y, desc_w, desc_h)

        self.description.setFont(QFont('DFkai-sb', 14))
        self.description.setStyleSheet('''
            border: solid black;
            border-width: 3px 3px 3px 3px;
        ''')

        # 4. 設定測驗科目的標籤
        subject_x = int(self.width() // 2)
        subject_h = 30
        self.subject_title.setGeometry(subject_x - int(start_x // 2), desc_y, subject_x, subject_h)
        self.subject_title.setFont(QFont('DFkai-sb', 18))
        self.subject_title.setStyleSheet('''
            border: solid black;
            border-width: 3px 3px 3px 3px;
        ''')

    def ui(self):
        # 設定初始畫面的標題
        self.init_title.setText('教  檢  測  驗  系  統')

        # windows size select
        self.label_size.setText('選擇視窗大小：')
        self.small.setChecked(True)
        self.small.setText('960x720')
        self.median.setText('1200x768')
        self.large.setText('1600x900')

        self.winsize_group.addButton(self.small, id=1)
        self.winsize_group.addButton(self.median, id=2)
        self.winsize_group.addButton(self.large, id=3)

        self.winsize_group.buttonClicked.connect(self._win_select_event)

        # description text
        self.description.setReadOnly(True)  # Read Only
        self.description.setPlainText('''操作說明：\n1. 下方選擇觀看合適的視窗大小\n2. 在測驗科目中, 選擇想測驗的科目\n\
3. 在選擇範圍中, 選擇想測驗的試卷年份\n4. 確定選擇正確後, 點選開始測驗的按鈕\n\n版本說明：\n''')
        pass

        # subject title text
        self.subject_title.setText('測驗科目：')

    def _win_select_event(self):
        select_id = self.winsize_group.checkedId()
        if select_id == 1:
            self.setFixedSize(960, 720)
        elif select_id == 2:
            self.setFixedSize(1200, 768)
        elif select_id == 3:
            self.setFixedSize(1600, 900)

        self._windows_setting()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = InitialWindow()
    window.show()
    sys.exit(app.exec_())
