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

        # 設定 5 個科目的按鈕變數
        self.subjects_group = QtWidgets.QButtonGroup(self)
        self.chinese_btn = QtWidgets.QRadioButton(self)
        self.math_btn = QtWidgets.QRadioButton(self)
        self.espr_btn = QtWidgets.QRadioButton(self)   # 教育理念與實務
        self.esdng_btn = QtWidgets.QRadioButton(self)  # 學習者發展與適性輔導
        self.escnt_btn = QtWidgets.QRadioButton(self)  # 課程教學與評量

        # 設定選擇年份的下拉式選單 & 標籤變數
        self.years_label = QtWidgets.QLabel(self)
        self.years_menu = QtWidgets.QComboBox(self)

        # 設定進入測驗的按鈕
        self.enter_test_btn = QtWidgets.QPushButton(self)

        # 顯示考試資訊的標籤
        self.test_info = QtWidgets.QLabel(self)

        # 各項科目的數值設定 (key 等於 subjects_group.checkedId())
        self.values = {
            10: {"subject": "國語文能力測驗", "time": '100'},
            20: {"subject": "數學能力測驗", "time": '80'},
            30: {"subject": "教育理念與實務", "time": '80'},
            40: {"subject": "學習者發展與適性輔導", "time": '80'},
            50: {"subject": "課程教學與評量", "time": '80'}
        }
        # -----

        self._windows_setting()
        self.ui()

    def _windows_setting(self):
        # 讓視窗在螢幕正中間顯示
        screen = QtWidgets.QApplication.desktop()
        screen_width, screen_height = screen.width(), screen.height()
        width, height = self.width(), self.height()
        self.move((screen_width - width) // 2, (screen_height - height) // 2)

        # QSS 設定
        ch_font = QFont('標楷體', 14)
        num_font = QFont('Times New Roman', 14)

        # 利用視窗大小, 計算每個元件的相對位置 & 設定 CSS 樣式
        # 1. 初始畫面標題
        init_title_h = int(height // 4)
        self.init_title.setGeometry(0, 0, width, init_title_h)

        self.init_title.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignJustify)
        self.init_title.setFont(QFont('標楷體'))
        self.init_title.setStyleSheet(
            '''
            color: black;
            font-size: 48px;
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
        # self.label_size.setStyleSheet('''
        #     border: solid black;
        #     border-width: 3px 3px 3px 3px;
        # ''')

        self.label_size.setFont(QFont('DFkai-sb', 18))
        self.small.setFont(num_font)
        self.median.setFont(num_font)
        self.large.setFont(num_font)

        # 3. 設定輸入框的大小和位置
        desc_y = init_title_h + 20  # 在標題底下的 20 px
        desc_w = int(self.width() // 2) - start_x  # 和 btn group 對齊
        desc_h = int(self.height() * 2 // 4)
        self.description.setGeometry(int(start_x // 2), desc_y, desc_w, desc_h)

        self.description.setFont(ch_font)
        # self.description.setStyleSheet('''
        #     border: solid black;
        #     border-width: 3px 3px 3px 3px;
        # ''')

        # 4. 設定測驗科目的標籤
        subject_x = int(self.width() // 2) - int(start_x // 4)
        subject_w = int(subject_x // 2)
        subject_h = 30
        self.subject_title.setGeometry(subject_x, desc_y, subject_w, subject_h)
        self.subject_title.setFont(QFont('DFkai-sb', 18))
        # self.subject_title.setStyleSheet('''
        #     border: solid black;
        #     border-width: 3px 3px 3px 3px;
        # ''')

        # 5. 設定測驗科目選單的位置
        subject_btn_w = int(subject_x // 2)
        subject_btn_y = init_title_h + 50
        self.chinese_btn.setGeometry(subject_x, subject_btn_y, subject_btn_w, subject_h)
        self.math_btn.setGeometry(subject_x, subject_btn_y + subject_h, subject_btn_w, subject_h)
        self.espr_btn.setGeometry(subject_x, subject_btn_y + 2 * subject_h, subject_btn_w, subject_h)
        self.esdng_btn.setGeometry(subject_x, subject_btn_y + 3 * subject_h, subject_btn_w, subject_h)
        self.escnt_btn.setGeometry(subject_x, subject_btn_y + 4 * subject_h, subject_btn_w, subject_h)

        self.chinese_btn.setFont(ch_font)
        self.math_btn.setFont(ch_font)
        self.espr_btn.setFont(ch_font)
        self.esdng_btn.setFont(ch_font)
        self.escnt_btn.setFont(ch_font)

        # 6. 設定選擇範圍的標籤
        self.years_label.setGeometry(subject_w + subject_x, desc_y, subject_w, subject_h)
        self.years_label.setFont(QFont('DFkai-sb', 18))

        # 7. 設定下拉式選單位置
        self.years_menu.setGeometry(subject_w + subject_x, subject_btn_y + 10, int(subject_w * 3 // 4), subject_h)
        self.years_menu.setFont(QFont('Times New Roman', 14))

        # 8. 設定進入測驗按鈕位置
        test_btn_x = subject_w + subject_x + int(subject_w * 1 // 4)
        test_btn_h = 40
        self.enter_test_btn.setGeometry(test_btn_x, self.height() - test_btn_h * 3, int(subject_w // 2), test_btn_h)
        self.enter_test_btn.setFont(ch_font)

        # 9. 顯示測驗考卷資訊
        test_info_y = int(self.height() * 0.7)
        test_info_w = int(subject_x * 3 // 4)
        self.test_info.setGeometry(subject_x, test_info_y, test_info_w, self.height() - test_info_y)
        self.test_info.setFont(QFont('標楷體', 13))

    def ui(self):
        # 設定初始畫面的標題
        self.init_title.setText('教  檢  歷  屆  試  題  測  驗  系  統')

        # windows size select
        self.label_size.setText('選擇視窗大小：')
        self.small.setChecked(True)
        self.small.setText('960x720')
        self.median.setText('1200x768')
        self.large.setText('1440x960')

        self.winsize_group.addButton(self.small, id=1)
        self.winsize_group.addButton(self.median, id=2)
        self.winsize_group.addButton(self.large, id=3)

        self.winsize_group.buttonClicked.connect(self._win_select_event)

        # description text
        self.description.setReadOnly(True)  # Read Only
        self.description.setPlainText('''介面說明：\n1. 下方選擇觀看合適的視窗大小\n2. 在測驗科目中, 選擇想測驗的科目\n\
3. 在選擇範圍中, 選擇想測驗的試卷年份\n4. 確定選擇正確後, 點選開始測驗的按鈕\n\n版本說明：\n''')
        pass

        # subject title text
        self.subject_title.setText('測驗科目：')

        # subjects select
        self.chinese_btn.setText('國語文能力測驗')
        self.math_btn.setText('數學能力測驗')
        self.espr_btn.setText('教育理念與實務')
        self.esdng_btn.setText('學習者發展與適性輔導')
        self.escnt_btn.setText('課程教學與評量')

        self.subjects_group.addButton(self.chinese_btn, id=10)
        self.subjects_group.addButton(self.math_btn, id=20)
        self.subjects_group.addButton(self.espr_btn, id=30)
        self.subjects_group.addButton(self.esdng_btn, id=40)
        self.subjects_group.addButton(self.escnt_btn, id=50)

        self.subjects_group.buttonClicked.connect(self._subject_select_event)
        # print(self.subjects_group.checkedId())  # 全部都沒選擇 checkedId 的值 = -1

        # years title text
        self.years_label.setText('選擇範圍：')

        # years menu item
        # 數學僅從 103 年開始考 和 subject 選擇相關, 因此直接在 _subject_select_event 設定

        # enter test button
        self.enter_test_btn.setText("進入測驗")

        # test information label(和 subject 有關係, 在 _subject_select_event 設定)

    def _win_select_event(self):
        select_id = self.winsize_group.checkedId()
        if select_id == 1:
            self.setFixedSize(960, 720)
        elif select_id == 2:
            self.setFixedSize(1200, 768)
        elif select_id == 3:
            self.setFixedSize(1440, 960)

        self._windows_setting()  # 重新整理視窗介面

    def _year_select_event(self):
        select_id = self.subjects_group.checkedId()

        # test information label
        test_subject, test_time = self.values[select_id]["subject"], self.values[select_id]["time"]
        if self.years_menu.currentIndex() == 0:
            test_range = " "
        else:
            test_range = self.years_menu.currentText()
        self.test_info.setText(f'作答科目：{test_subject}\n作答時間：{test_time} 分鐘\n測驗範圍：{test_range} 年')
        pass

    def _subject_select_event(self):
        select_id = self.subjects_group.checkedId()

        # 設定選擇範圍下拉式選單的值, 數學僅從 103 年開始
        if select_id == 20:
            lst = [str(i) for i in range(103, 113)]
        else:
            lst = [str(i) for i in range(94, 113)]
            lst.append("103 ~ 112")

        lst.insert(0, "請選擇年份")
        lst.append("94 ~ 102")
        lst.append("全選")

        self.years_menu.clear()  # 要清除先前的下拉式選單選項, 才不會一直疊加
        self.years_menu.addItems(lst)
        self.years_menu.currentIndexChanged.connect(self._year_select_event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = InitialWindow()
    window.show()
    sys.exit(app.exec_())
