from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QFont, QPixmap, QPalette, QColor
from json import load, dump
from datetime import datetime
from time import sleep
import os
import sys

# 之後可以根據使用者選的選項之後, 再 import 特定的檔案和答案
import Question.ChineseQ as chineseQ
import Question.MathQ as mathQ
import Question.EsprQ as esprQ
import Question.EsdngQ as esdngQ
import Question.EscntQ as escntQ


# 各年各科目的測驗題數(去除 107 年)
# 去除作文
Chinese = {
    "94": {"ChooseQ": 35},
    "95": {"ChooseQ": 35},
    "96": {"ChooseQ": 35},
    "97": {"ChooseQ": 35},
    "98": {"ChooseQ": 35},
    "99": {"ChooseQ": 30},
    "100": {"ChooseQ": 30},
    "101": {"ChooseQ": 30},
    "102": {"ChooseQ": 30},
    "103": {"ChooseQ": 30},
    "104": {"ChooseQ": 30},
    "105": {"ChooseQ": 30},
    "106": {"ChooseQ": 30},
    "108-1": {"ChooseQ": 30},
    "108-2": {"ChooseQ": 30},
    "109": {"ChooseQ": 30},
    "110": {"ChooseQ": 25, "MultiQ": 10},
    "111": {"ChooseQ": 25, "MultiQ": 6},
    "112": {"ChooseQ": 25, "MultiQ": 4}
}

Math = {
    "103": {"ChooseQ": 30, "NotChooseQ": 11},
    "104": {"ChooseQ": 30, "NotChooseQ": 11},
    "105": {"ChooseQ": 30, "NotChooseQ": 8},
    "106": {"ChooseQ": 30, "NotChooseQ": 8},
    "108-1": {"ChooseQ": 30, "NotChooseQ": 8},
    "108-2": {"ChooseQ": 30, "NotChooseQ": 8},
    "109": {"ChooseQ": 30, "NotChooseQ": 8},
    "110": {"ChooseQ": 26, "NotChooseQ": 6, "MultiQ": 8},
    "111": {"ChooseQ": 26, "NotChooseQ": 6, "MultiQ": 8},
    "112": {"ChooseQ": 26, "NotChooseQ": 6, "MultiQ": 4}
}

Espr = {
    "94": {"ChooseQ": 40, "QA": 4},
    "95": {"ChooseQ": 40, "QA": 4},
    "96": {"ChooseQ": 40, "QA": 4},
    "97": {"ChooseQ": 40, "QA": 4},
    "98": {"ChooseQ": 40, "QA": 4},
    "99": {"ChooseQ": 40, "QA": 4},
    "100": {"ChooseQ": 40, "QA": 4},
    "101": {"ChooseQ": 40, "QA": 4},
    "102": {"ChooseQ": 40, "QA": 4},
    "103": {"ChooseQ": 40, "QA": 4},
    "104": {"ChooseQ": 40, "QA": 4},
    "105": {"ChooseQ": 40, "QA": 4},
    "106": {"ChooseQ": 40, "QA": 4},
    "108-1": {"ChooseQ": 40, "QA": 4},
    "108-2": {"ChooseQ": 40, "QA": 4},
    "109": {"ChooseQ": 40, "QA": 4},
    "110": {"ChooseQ": 25, "QA": 3, "MultiQ": 4},
    "111": {"ChooseQ": 25, "QA": 3, "MultiQ": 6},
    "112": {"ChooseQ": 25, "QA": 3, "MultiQ": 3}
}

Esdng = {
    "94": {"ChooseQ": 50, "QA": 3},
    "95": {"ChooseQ": 35, "QA": 3},
    "96": {"ChooseQ": 35, "QA": 3},
    "97": {"ChooseQ": 35, "QA": 3},
    "98": {"ChooseQ": 35, "QA": 3},
    "99": {"ChooseQ": 35, "QA": 3},
    "100": {"ChooseQ": 35, "QA": 3},
    "101": {"ChooseQ": 35, "QA": 3},
    "102": {"ChooseQ": 35, "QA": 3},
    "103": {"ChooseQ": 30, "QA": 4},
    "104": {"ChooseQ": 30, "QA": 4},
    "105": {"ChooseQ": 30, "QA": 4},
    "106": {"ChooseQ": 30, "QA": 4},
    "108-1": {"ChooseQ": 30, "QA": 4},
    "108-2": {"ChooseQ": 30, "QA": 4},
    "109": {"ChooseQ": 30, "QA": 4},
    "110": {"ChooseQ": 25, "QA": 3, "MultiQ": 5},
    "111": {"ChooseQ": 25, "QA": 3, "MultiQ": 7},
    "112": {"ChooseQ": 25, "QA": 3, "MultiQ": 4}
}

Escnt = {
    "94": {"ChooseQ": 36, "QA": 4},
    "95": {"ChooseQ": 36, "QA": 4},
    "96": {"ChooseQ": 36, "QA": 4},
    "97": {"ChooseQ": 36, "QA": 4},
    "98": {"ChooseQ": 35, "QA": 3},
    "99": {"ChooseQ": 35, "QA": 3},
    "100": {"ChooseQ": 35, "QA": 3},
    "101": {"ChooseQ": 35, "QA": 3},
    "102": {"ChooseQ": 35, "QA": 3},
    "103": {"ChooseQ": 30, "QA": 4},
    "104": {"ChooseQ": 30, "QA": 4},
    "105": {"ChooseQ": 30, "QA": 4},
    "106": {"ChooseQ": 30, "QA": 4},
    "108-1": {"ChooseQ": 30, "QA": 4},
    "108-2": {"ChooseQ": 30, "QA": 4},
    "109": {"ChooseQ": 30, "QA": 4},
    "110": {"ChooseQ": 25, "QA": 3, "MultiQ": 5},
    "111": {"ChooseQ": 25, "QA": 3, "MultiQ": 5},
    "112": {"ChooseQ": 25, "QA": 3, "MultiQ": 5}
}

TEST_SUBJECTS = [Chinese, Math, Espr, Esdng, Escnt]


class InitialWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("教師資格考試測驗系統")
        self.setWindowIcon(QtGui.QIcon("./image/windowsicon.ico"))
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        # 初始螢幕視窗大小(固定)
        self.setFixedSize(1600, 900)

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
            0: {"subject": "國語文能力測驗", "time": 100},
            1: {"subject": "數學能力測驗", "time": 80},
            2: {"subject": "教育理念與實務", "time": 80},
            3: {"subject": "學習者發展與適性輔導", "time": 80},
            4: {"subject": "課程教學與評量", "time": 80}
        }

        # 設定收藏題目的按鈕
        self.collection_btn = QtWidgets.QPushButton(self)

        # 設定 Message Box 變數
        self.test_msgbox = QtWidgets.QMessageBox(self)

        # 測驗視窗的變數
        self.quiz_windows = None
        self.collection_windows = None
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

        self.init_title.setAlignment(QtCore.Qt.AlignCenter)
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

        self.label_size.setFont(QFont('DFkai-sb', 18))
        self.small.setFont(num_font)
        self.median.setFont(num_font)
        self.large.setFont(num_font)

        # 3. 設定輸入框的大小和位置
        desc_y = init_title_h + 20  # 在標題底下的 20 px
        desc_w = int(self.width() // 2) - start_x  # 和 btn group 對齊
        desc_h = int(self.height() * 2 // 4)
        self.description.setGeometry(int(start_x // 2), desc_y, desc_w, desc_h)

        self.description.setFont(QFont('標楷體', 12))
        # - 設定 輸入框的背景是透明的
        palette = self.palette()
        palette.setColor(QPalette.Base, QColor(0, 0, 0, 0))
        self.description.setPalette(palette)

        self.description.setStyleSheet('''
            border: 1px solid gray;
        ''')

        # 4. 設定測驗科目的標籤
        subject_x = int(self.width() // 2) - int(start_x // 4)
        subject_w = int(subject_x // 2)
        subject_h = 30
        self.subject_title.setGeometry(subject_x, desc_y, subject_w, subject_h)
        self.subject_title.setFont(QFont('DFkai-sb', 18))

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
        test_btn_x = int(subject_w * 1.25) + subject_x
        test_btn_h = 40

        self.enter_test_btn.setGeometry(test_btn_x, self.height() - test_btn_h * 3, int(subject_w // 2), test_btn_h)
        self.enter_test_btn.setFont(ch_font)

        # 9. 顯示查看收藏題目的按鈕位置
        self.collection_btn.setGeometry(test_btn_x, self.height() - test_btn_h * 5, int(subject_w // 2), test_btn_h)
        self.collection_btn.setFont(ch_font)

        # 10. 顯示測驗考卷資訊的位置
        test_info_y = int(self.height() * 0.7)
        test_info_w = int(subject_x * 3 // 5)
        self.test_info.setGeometry(subject_x, test_info_y, test_info_w, self.height() - test_info_y)
        self.test_info.setFont(QFont('標楷體', 13))

        # 10. 設定 QMessageBox 位置
        self.test_msgbox.setStyleSheet('''font-size: 16px;''')

    def ui(self):
        # 設定初始畫面的標題
        self.init_title.setText('國 民 小 學 - 教 檢 歷 屆 試 題 系 統')

        # windows size select
        self.label_size.setText('選擇視窗大小：')
        self.median.setChecked(True)
        self.small.setText('1200x768')
        self.median.setText('1600x900')
        self.large.setText('1920x1080')

        self.winsize_group.addButton(self.small, id=1)
        self.winsize_group.addButton(self.median, id=2)
        self.winsize_group.addButton(self.large, id=3)

        self.winsize_group.buttonClicked.connect(self._win_select_event)

        # description text
        self.description.setReadOnly(True)  # Read Only
        self.description.setPlainText('''介面說明：\n1. 下方選擇觀看合適的視窗大小\n2. 在測驗科目中, 選擇想測驗的科目\n\
3. 在選擇範圍中, 選擇想測驗的試卷年份\n4. 確定選擇正確後, 點選進入測驗的按鈕\n5. 再次確認考試資訊無誤後, 點選確認進入正式測驗\n\n版本說明：
v1.1：新增課程教學與評量 108-1、108-2、109、110 年，學習者發展與適性輔導 110 年，新增教育理念與實務 110 年試卷 
v1.0：處理選項和題目皆有圖片的問題
beta v2.1：新增國文 112 年試卷，修正顯示圖片後沒有選項的問題
beta v2.0：新增教育理念與實務、學習者發展與適性輔導、課程教學與評量 111、112 年試卷\n''')
        pass

        # subject title text
        self.subject_title.setText('測驗科目：')

        # subjects select
        self.chinese_btn.setText('國語文能力測驗')
        self.math_btn.setText('數學能力測驗')
        self.espr_btn.setText('教育理念與實務')
        self.esdng_btn.setText('學習者發展與適性輔導')
        self.escnt_btn.setText('課程教學與評量')

        self.subjects_group.addButton(self.chinese_btn, id=0)
        self.subjects_group.addButton(self.math_btn, id=1)
        self.subjects_group.addButton(self.espr_btn, id=2)
        self.subjects_group.addButton(self.esdng_btn, id=3)
        self.subjects_group.addButton(self.escnt_btn, id=4)

        self.subjects_group.buttonClicked.connect(self._subject_select_event)
        # print(self.subjects_group.checkedId())  # 全部都沒選擇 checkedId 的值 = -1

        # years title text
        self.years_label.setText('選擇範圍：')

        # years menu item
        # 數學僅從 103 年開始考 和 subject 選擇相關, 因此直接在 _subject_select_event 設定
        # test information label(和 subject 有關係, 在 _subject_select_event 設定)

        # enter test button
        self.enter_test_btn.setText("進入測驗")
        self.enter_test_btn.setEnabled(False)  # 預設按鈕不可點

        # collection button
        self.collection_btn.setText('查看已收藏題目')
        self.collection_btn.clicked.connect(self._collection_clicked)

        # 新增自訂義按鈕
        sure = QtWidgets.QPushButton("確定")
        cancel = QtWidgets.QPushButton("取消")
        self.test_msgbox.addButton(sure, QtWidgets.QMessageBox.AcceptRole)
        self.test_msgbox.addButton(cancel, QtWidgets.QMessageBox.RejectRole)

        self.enter_test_btn.clicked.connect(self._enter_test_event)

    def _win_select_event(self):
        select_id = self.winsize_group.checkedId()
        if select_id == 1:
            self.setFixedSize(1200, 768)
        elif select_id == 2:
            self.setFixedSize(1600, 900)
        elif select_id == 3:
            self.setFixedSize(1920, 1080)

        self._windows_setting()  # 重新整理視窗介面

    def _year_select_event(self):
        select_id = self.subjects_group.checkedId()

        # test information label
        test_subject, test_time = self.values[select_id]["subject"], self.values[select_id]["time"]
        if self.years_menu.currentIndex() <= 0:
            test_range = " "
            choice_num = " "
            self.enter_test_btn.setEnabled(False)

        else:
            test_range = self.years_menu.currentText()
            choice_num = TEST_SUBJECTS[select_id][test_range]['ChooseQ']
            self.enter_test_btn.setEnabled(True)  # 上面資訊都填完時, 進入測驗的按鈕才可以按下

        self.test_info.setText(f'作答科目：{test_subject}\n作答時間：{test_time} 分鐘\n測驗試卷：{test_range}\n選擇題數：{choice_num} 題')
        pass

    def _subject_select_event(self):
        select_id = self.subjects_group.checkedId()

        # 設定選擇範圍下拉式選單的值, 數學僅從 103 年開始
        # if select_id == 1:
        #     lst = [str(i) for i in range(112, 102, -1)]
        # else:
        #     lst = [str(i) for i in range(112, 93, -1)]
        #     # lst.append("103 ~ 112")

        # 先根據現有的考卷去設定下拉式選單
        if select_id == 0:
            lst = [str(i) for i in range(112, 111, -1)]
        elif select_id == 1:
            lst = [str(i) for i in range(112, 111, -1)]
        elif select_id == 2:
            lst = [str(i) for i in range(112, 109, -1)]
        elif select_id == 3:
            lst = [str(i) for i in range(112, 109, -1)]
        elif select_id == 4:
            lst = [str(i) for i in range(112, 106, -1)]
            lst[lst.index('107')] = '108-1'
            lst[lst.index('108')] = '108-2'
        else:
            lst = []

        lst.insert(0, "請選擇年份")
        # 去除 107 題目, 和區分 108 年兩份試卷
        # lst[lst.index('107')] = '108-1'
        # lst[lst.index('108')] = '108-2'

        self.years_menu.clear()  # 要清除先前的下拉式選單選項, 才不會一直疊加
        self.years_menu.addItems(lst)
        self.years_menu.currentIndexChanged.connect(self._year_select_event)

    def _collection_clicked(self):
        self.collection_windows = CollectionQWindows(
            windows_size=(self.width(), self.height()),
            font_size=10 + self.winsize_group.checkedId() * 2,
            initWindow=self
        )
        self.collection_windows.show()
        self.close()

    def _enter_test_event(self):
        text = self.test_info.text()

        self.test_msgbox.setWindowTitle('測驗資訊')
        self.test_msgbox.setIcon(QtWidgets.QMessageBox.Information)
        self.test_msgbox.setText(text)

        result = self.test_msgbox.exec_()

        # 在這邊會銜接開啟測驗視窗
        if result == 0:
            # 將初始視窗設定的參數傳給第二個視窗
            self.quiz_windows = QuizWindows(
                windows_size=(self.width(), self.height()),
                subject_info=self.values[self.subjects_group.checkedId()],
                subject_select_id=self.subjects_group.checkedId(),
                test_year=self.years_menu.currentText(),
                test_year_id=self.years_menu.currentIndex(),
                font_size=10 + self.winsize_group.checkedId() * 2,
                initWindow=self
            )
            self.quiz_windows.show()
            self.close()


class QuizWindows(QtWidgets.QWidget):
    def __init__(self, **kwargs):
        super(QuizWindows, self).__init__()

        self.setWindowTitle("教師資格考試測驗系統")
        self.setWindowIcon(QtGui.QIcon("./image/windowsicon.ico"))
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        # 設定視窗大小並固定在螢幕正中間出現
        windows = kwargs['windows_size']
        self.width, self.height = windows
        self.setFixedSize(self.width, self.height)

        screen = QtWidgets.QApplication.desktop()
        screen_width, screen_height = screen.width(), screen.height()
        self.move((screen_width - self.width) // 2, (screen_height - self.height) // 2)

        # 初始視窗的參數
        self.parameters = kwargs
        self.setFont(QFont('細明體', kwargs["font_size"]))

        # -- 初始視窗
        self.initWindow = kwargs["initWindow"]

        # ----- 參數設定 -----
        # 設定選項內容的變數(文字/圖片放在 Label 裡面呈現)
        self.option_group = QtWidgets.QButtonGroup(self)
        self.btn_A = QtWidgets.QRadioButton(self)
        self.btn_B = QtWidgets.QRadioButton(self)
        self.btn_C = QtWidgets.QRadioButton(self)
        self.btn_D = QtWidgets.QRadioButton(self)

        self.text_A = QtWidgets.QLabel(self)
        self.text_B = QtWidgets.QLabel(self)
        self.text_C = QtWidgets.QLabel(self)
        self.text_D = QtWidgets.QLabel(self)

        # 設定可以快速跳轉到某一頁的選單
        self.page_goto = QtWidgets.QComboBox(self)

        # 設定前/後一頁的按鈕
        self.previous_btn = QtWidgets.QPushButton(self)
        self.next_btn = QtWidgets.QPushButton(self)

        # 顯示剩餘時間的變數
        # - 測驗時間
        self.quiz_time = kwargs["subject_info"]["time"] * 60  # 單位: 秒
        self.current_time = kwargs["subject_info"]["time"] * 60

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self._timer_count)
        self.timer_label = QtWidgets.QLabel(self)
        self.timer_pause_btn = QtWidgets.QPushButton(self)

        # 設定題目內容及相關的變數
        self.question_text = QtWidgets.QTextEdit(self)
        self.question_image = QtWidgets.QLabel(self)

        # 處理 import 試卷的區域, 和答案的 JSON 檔案路徑(給以後需要設計練習模式時使用)
        index, years, year_id = kwargs["subject_select_id"], kwargs["test_year"], kwargs["test_year_id"]
        # TEST_SUBJECTS = [Chinese, Math, Espr, Esdng, Escnt]
        if index == 0:
            # 國文試卷
            self.questions = chineseQ.YEARS[year_id - 1]
            self.answers_data_path = "./Answer/ChineseA.json"
        elif index == 1:
            # 數學試卷
            self.questions = mathQ.YEARS[year_id - 1]
            self.answers_data_path = "./Answer/MathA.json"
        elif index == 2:
            # espr 試卷, 教育理念與實務
            self.questions = esprQ.YEARS[year_id - 1]
            self.answers_data_path = "./Answer/EsprA.json"
        elif index == 3:
            # esdng 試卷, 學習者發展與適性輔導
            self.questions = esdngQ.YEARS[year_id - 1]
            self.answers_data_path = "./Answer/EsdngA.json"
        elif index == 4:
            # escnt 試卷, 課程教學與評量
            self.questions = escntQ.YEARS[year_id - 1]
            self.answers_data_path = "./Answer/EscntA.json"

        self.current_question = 1  # 存放當前顯示的題目
        self.questions_number = TEST_SUBJECTS[index][years]["ChooseQ"]
        self.user_answers = [0] * self.questions_number

        # 收藏題目的變數
        self.collectionQ = list()
        self.isCollect = 0  # 控制開關
        self.collection_label = QtWidgets.QLabel(self)

        # 交卷的變數
        self.send_answer_btn = QtWidgets.QPushButton(self)
        self.result_window = None  # 新視窗的變數
        # -----

        self._window_setting()
        self.ui()

    def _window_setting(self):
        width, height = self.width, self.height

        # 1. 設定題目文字位置
        q_text_x, q_text_w = int(width * 0.02), int(width * 0.95)
        q_text_y = int(height * 0.02)
        isImage = self.questions[self.current_question]["isImage"]

        if isImage == "" or isImage == "A":
            # 題目無圖片
            q_text_h = int(height * 0.5)
        else:
            # 題目有圖片
            q_text_h = int(height * 0.23)
            # 2. 設定題目圖片/表格位置
            q_img_y, q_img_h = int(height * 0.26), int(height * 0.3)
            self.question_image.setGeometry(q_text_x, q_img_y, q_text_w, q_img_h)
            self.question_image.setAlignment(QtCore.Qt.AlignLeft)

        self.question_text.setGeometry(q_text_x, q_text_y, q_text_w, q_text_h)

        palette = self.palette()
        palette.setColor(QPalette.Base, QColor(0, 0, 0, 0))
        self.question_text.setPalette(palette)

        self.question_text.setFont(QFont('細明體', self.parameters["font_size"]))
        self.question_text.setStyleSheet('''
            border: none;
        ''')
        self.question_text.setAlignment(QtCore.Qt.AlignLeft)

        # 3. 設定選項 A, B, C, D & 各 Label 的位置(若有圖片, 盡量找可以 resize image 的方法)
        btnA_y, btn_w, btn_h = int(height * 0.6), 20, 20
        self.btn_A.setGeometry(q_text_x, btnA_y, btn_w, btn_h)
        textA_w, textA_h = int(width * 0.3), int(height * 0.18)
        self.text_A.setGeometry(q_text_x + btn_w, btnA_y, textA_w, textA_h)
        self.text_A.setAlignment(QtCore.Qt.AlignLeft)

        btnB_x = int(width * 0.4)
        self.btn_B.setGeometry(btnB_x, btnA_y, btn_w, btn_h)
        self.text_B.setGeometry(btnB_x + btn_w, btnA_y, textA_w, textA_h)
        self.text_B.setAlignment(QtCore.Qt.AlignLeft)

        btnC_y = int(height * 0.78)
        self.btn_C.setGeometry(q_text_x, btnC_y + btn_h, btn_w, btn_h)
        self.text_C.setGeometry(q_text_x + btn_w, btnA_y + textA_h + btn_h, textA_w, textA_h)
        self.text_C.setAlignment(QtCore.Qt.AlignLeft)

        self.btn_D.setGeometry(btnB_x, btnC_y + btn_h, btn_w, btn_h)
        self.text_D.setGeometry(btnB_x + btn_w, btnA_y + textA_h + btn_h, textA_w, textA_h)
        self.text_D.setAlignment(QtCore.Qt.AlignLeft)

        # 3. 設定前/後一頁按鈕位置
        page_btn_x = btnB_x + textA_w + 4 * btn_w
        page_btn_w = int(width * 0.08)
        page_btn_h = int(height * 0.05)
        self.previous_btn.setGeometry(page_btn_x, btnA_y, page_btn_w, page_btn_h)
        self.next_btn.setGeometry(page_btn_x + page_btn_w + 10, btnA_y, page_btn_w, page_btn_h)

        # 4. 設定下拉式選單位置
        page_goto_w = int(width * 0.11)
        page_goto_y = btnA_y + int(page_btn_h * 1.2)

        self.page_goto.setGeometry(page_btn_x, page_goto_y, page_goto_w, page_btn_h)

        # 5. 設定 timer 的標籤文字位置
        timer_label_y = page_goto_y + page_btn_h + 20
        self.timer_label.setGeometry(page_btn_x, timer_label_y, page_btn_w * 2, page_btn_h)

        # 6. 設定 timer pause btn 的樣式
        pixmap = QtGui.QPixmap('./image/icon_pause.png')
        icon = QtGui.QIcon(pixmap)
        self.timer_pause_btn.setIcon(icon)
        self.timer_pause_btn.setGeometry(page_btn_x, timer_label_y + page_btn_h, pixmap.width(), pixmap.height())

        # 7. 設定 collection btn 的樣式 (設定在下拉式選單的旁邊)
        pixmap2 = QtGui.QPixmap('./image/icon_black_star.png')
        pixmap2 = pixmap2.scaled(page_btn_h, page_btn_h)
        self.collection_label.setPixmap(pixmap2)
        self.collection_label.setGeometry(page_btn_x + page_goto_w + 40, page_goto_y, page_btn_h, page_btn_h)

        # 8. 交卷按鈕位置
        send_btn_x, send_btn_y = page_btn_x + page_btn_w + 10, page_goto_y + page_btn_h * 5
        send_btn_w, send_btn_h = int(width * 0.1), int(height * 0.05)
        self.send_answer_btn.setFont(QFont('細明體', 14))
        self.send_answer_btn.setGeometry(send_btn_x, send_btn_y, send_btn_w, send_btn_h)

    def ui(self):
        # 設定 question_text & image 內容(未來要抓題目的資料)
        self.question_text.setReadOnly(True)
        self._questions_setting()

        # 設定點選標籤也可以選擇該選項
        self.text_A.enterEvent = self._mouse_cursor_enter
        self.text_A.mousePressEvent = self._label_option_a_clicked
        self.text_A.leaveEvent = self._mouse_cursor_leave

        self.text_B.enterEvent = self._mouse_cursor_enter
        self.text_B.mousePressEvent = self._label_option_b_clicked
        self.text_B.leaveEvent = self._mouse_cursor_leave

        self.text_C.enterEvent = self._mouse_cursor_enter
        self.text_C.mousePressEvent = self._label_option_c_clicked
        self.text_C.leaveEvent = self._mouse_cursor_leave

        self.text_D.enterEvent = self._mouse_cursor_enter
        self.text_D.mousePressEvent = self._label_option_d_clicked
        self.text_D.leaveEvent = self._mouse_cursor_leave

        # 設定 option btn A, B, C, D 以及相關滑鼠事件
        self.option_group.addButton(self.btn_A, id=1)
        self.option_group.addButton(self.btn_B, id=2)
        self.option_group.addButton(self.btn_C, id=3)
        self.option_group.addButton(self.btn_D, id=4)

        self.btn_A.enterEvent = self._mouse_cursor_enter
        self.btn_A.leaveEvent = self._mouse_cursor_leave

        self.btn_B.enterEvent = self._mouse_cursor_enter
        self.btn_B.leaveEvent = self._mouse_cursor_leave

        self.btn_C.enterEvent = self._mouse_cursor_enter
        self.btn_C.leaveEvent = self._mouse_cursor_leave

        self.btn_D.enterEvent = self._mouse_cursor_enter
        self.btn_D.leaveEvent = self._mouse_cursor_leave

        self._restore_option_choice()
        self.option_group.buttonClicked.connect(self._option_choice_event)

        # 設定 previous/next page 的按鈕
        self.previous_btn.setText('上一題')
        self.previous_btn.clicked.connect(self._previous_question)
        self.previous_btn.setEnabled(False)

        self.next_btn.setText('下一題')
        self.next_btn.clicked.connect(self._next_question)

        # 設定 page_goto 下拉式選單
        pages = self.questions_number

        self.page_goto.clear()
        self.page_goto.addItem('請選擇題數')
        self.page_goto.addItems([str(i) for i in range(1, pages + 1)])
        self.page_goto.currentIndexChanged.connect(self._page_goto_event)

        # 設定 timer 定時, 顯示標籤文字, 暫停/開始按鈕, 以及視窗
        self.timer.start(1000)  # 計時器
        self.timer_pause_btn.clicked.connect(self._timer_pause)

        # 設定收藏 Label 的事件
        self.collection_label.enterEvent = self._mouse_cursor_enter
        self.collection_label.mousePressEvent = self._collection_clicked
        self.collection_label.leaveEvent = self._mouse_cursor_leave

        # 設定交卷按鈕
        self.send_answer_btn.setText('交卷')
        self.send_answer_btn.clicked.connect(self._timer_pause)

        # 先跑過一次 _restore_collection_mark
        self._restore_collection_mark()

    def _questions_setting(self):
        key = self.current_question
        question = self.questions[key]
        q, options = question["Q"]["text"], question["Option"]
        q = str(key) + '. ' + q

        if question["isImage"] == "":
            A, B, C, D = options["A"]["text"], options["B"]["text"], options["C"]["text"], options["D"]["text"]
            self.text_A.setText(A)
            self.text_B.setText(B)
            self.text_C.setText(C)
            self.text_D.setText(D)

        elif question["isImage"] == "Q":
            A, B, C, D = options["A"]["text"], options["B"]["text"], options["C"]["text"], options["D"]["text"]
            self.text_A.setText(A)
            self.text_B.setText(B)
            self.text_C.setText(C)
            self.text_D.setText(D)

            # 題目有圖片
            q_img = QPixmap(question["Q"]["img"])
            self.question_image.setPixmap(q_img)

        elif question["isImage"] == "A":
            # 選項有圖片無文字
            img_a, img_b = QPixmap(options["A"]["img"]), QPixmap(options["B"]["img"])
            img_c, img_d = QPixmap(options["C"]["img"]), QPixmap(options["D"]["img"])

            # 讓圖片 Resize 成 QLabel 的大小
            if img_a.size().width() > self.text_A.size().width() or img_a.size().height() > self.text_A.size().height():
                img_a = img_a.scaled(self.text_A.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_b.size().width() > self.text_B.size().width() or img_b.size().height() > self.text_B.size().height():
                img_b = img_b.scaled(self.text_B.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_c.size().width() > self.text_C.size().width() or img_c.size().height() > self.text_C.size().height():
                img_c = img_c.scaled(self.text_C.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_d.size().width() > self.text_D.size().width() or img_d.size().height() > self.text_D.size().height():
                img_d = img_d.scaled(self.text_D.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            self.text_A.setPixmap(img_a)
            self.text_B.setPixmap(img_b)
            self.text_C.setPixmap(img_c)
            self.text_D.setPixmap(img_d)

        else:
            # 題目 & 選項都有圖片
            q_img = QPixmap(question["Q"]["img"])
            self.question_image.setPixmap(q_img)

            img_a, img_b = QPixmap(options["A"]["img"]), QPixmap(options["B"]["img"])
            img_c, img_d = QPixmap(options["C"]["img"]), QPixmap(options["D"]["img"])

            # 讓圖片 Resize 成 QLabel 的大小
            if img_a.size().width() > self.text_A.size().width() or img_a.size().height() > self.text_A.size().height():
                img_a = img_a.scaled(self.text_A.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_b.size().width() > self.text_B.size().width() or img_b.size().height() > self.text_B.size().height():
                img_b = img_b.scaled(self.text_B.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_c.size().width() > self.text_C.size().width() or img_c.size().height() > self.text_C.size().height():
                img_c = img_c.scaled(self.text_C.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_d.size().width() > self.text_D.size().width() or img_d.size().height() > self.text_D.size().height():
                img_d = img_d.scaled(self.text_D.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            self.text_A.setPixmap(img_a)
            self.text_B.setPixmap(img_b)
            self.text_C.setPixmap(img_c)
            self.text_D.setPixmap(img_d)

        self.question_text.setText(q)

    def _mouse_cursor_enter(self, event):
        self.setCursor(QtCore.Qt.PointingHandCursor)

    def _mouse_cursor_leave(self, event):
        self.setCursor(QtCore.Qt.ArrowCursor)

    def _update_question_image_state(self):
        # 更新題目圖片的狀態 question_image 的 state
        key = self.current_question
        question = self.questions[key]["Q"]
        if question["img"] == '':
            self.question_image.clear()

    def _label_option_a_clicked(self, event):
        self.btn_A.setChecked(True)
        self._option_choice_event()

    def _label_option_b_clicked(self, event):
        self.btn_B.setChecked(True)
        self._option_choice_event()

    def _label_option_c_clicked(self, event):
        self.btn_C.setChecked(True)
        self._option_choice_event()

    def _label_option_d_clicked(self, event):
        self.btn_D.setChecked(True)
        self._option_choice_event()

    def _option_choice_event(self):
        index = self.current_question - 1
        choose = self.option_group.checkedId()
        self.user_answers[index] = choose

    def _restore_option_choice(self):
        index = self.current_question - 1
        user_answer = self.user_answers[index]

        self.option_group.setExclusive(False)
        for i, btn in enumerate(self.option_group.buttons()):
            if user_answer == 0:
                # 更新 4 個選項的狀態, 全部變成未選取
                btn.setChecked(False)
            else:
                # 若該題目已被作答過, 則恢復成前次作答的選項狀態
                if i + 1 != user_answer:
                    btn.setChecked(False)
                else:
                    btn.setChecked(True)

        self.option_group.setExclusive(True)

    def _update_btn_state(self):
        if self.current_question == 1:
            self.previous_btn.setEnabled(False)
        else:
            self.previous_btn.setEnabled(True)

        if self.current_question >= self.questions_number:
            self.next_btn.setEnabled(False)
        else:
            self.next_btn.setEnabled(True)

    def _previous_question(self):
        self.current_question -= 1

        self._update_btn_state()
        self._restore_option_choice()
        self._window_setting()
        self._questions_setting()
        self._restore_collection_mark()
        self._update_question_image_state()

    def _next_question(self):
        self.current_question += 1

        self._update_btn_state()
        self._restore_option_choice()
        self._window_setting()
        self._questions_setting()
        self._restore_collection_mark()
        self._update_question_image_state()

    def _page_goto_event(self):
        self.current_question = self.page_goto.currentIndex()

        self._update_btn_state()
        self._restore_option_choice()
        self._window_setting()
        self._questions_setting()
        self._restore_collection_mark()
        self._update_question_image_state()

    def _timer_count(self):
        minute = str(self.current_time // 60)
        if self.current_time % 60 < 10:
            second = '0' + str(self.current_time % 60)
        else:
            second = str(self.current_time % 60)

        self.timer_label.setText(f'剩餘時間：{minute}分{second}秒')
        self.current_time = self.current_time - 1

    def _timer_start(self):
        self.timer.start(1000)  # 計時器

    def _timer_pause(self):
        self.timer.stop()

        # 創建一個 msg box 視窗, 用來讓時間繼續或交卷
        # - 在暫停測驗期間, 將測驗視窗隱藏
        self.hide()
        _hint_box = QtWidgets.QMessageBox(self)

        _hint_box.setWindowTitle("暫停測驗")
        reducingQ = str(self.user_answers.count(0))
        text = "當前" + self.timer_label.text() + "\n" + "剩餘未作答題數：" + reducingQ + "\n確認是否交卷？\n"
        _hint_box.setFont(QFont('細明體', 12))
        _hint_box.setText(text)
        _hint_box.setIcon(QtWidgets.QMessageBox.Information)

        back = QtWidgets.QPushButton("返回測驗")
        send = QtWidgets.QPushButton("交卷")

        _hint_box.addButton(back, QtWidgets.QMessageBox.AcceptRole)  # AcceptRole = 0, RejectRole = 1
        _hint_box.addButton(send, QtWidgets.QMessageBox.RejectRole)  # 交卷會開新的視窗

        isExitTest = _hint_box.exec_()
        if isExitTest == 0:
            self.show()
            self._timer_start()

        elif isExitTest == 1:
            self._send_answer_event()

    def _restore_collection_mark(self):
        subject = self.parameters["subject_info"]["subject"]
        year = self.parameters["test_year"]

        if os.path.exists("./_collection_question.json"):
            with open("./_collection_question.json") as json_file:
                history_collection = load(json_file)

                if subject in history_collection.keys():
                    years_list = history_collection[subject]["測驗年份"]
                    if year in years_list:
                        index = years_list.index(year)
                        question_list = history_collection[subject]["收藏題目"][index]
                    else:
                        question_list = self.collectionQ
                else:
                    question_list = self.collectionQ

            if self.current_question in question_list:
                self.isCollect = 1
                pixmap = QPixmap('./image/icon_yellow_star.png')
                pixmap = pixmap.scaled(self.collection_label.width(), self.collection_label.height())
                self.collection_label.setPixmap(pixmap)

            else:
                self.isCollect = 0

    def _collection_clicked(self, event):
        # 點選一下是將題目加入收藏, 若題目已加入收藏時, 再點一下是取消
        if self.isCollect == 0:
            self.isCollect = 1
            pixmap = QPixmap('./image/icon_yellow_star.png')
            pixmap = pixmap.scaled(self.collection_label.width(), self.collection_label.height())

            if self.current_question not in self.collectionQ:
                self.collectionQ.append(self.current_question)

        else:
            # 已經收藏過了, 又點擊則要取消收藏
            self.isCollect = 0
            pixmap = QPixmap('./image/icon_black_star.png')
            pixmap = pixmap.scaled(self.collection_label.width(), self.collection_label.height())

            self.collectionQ.remove(self.current_question)

        self.collection_label.setPixmap(pixmap)
        self.collectionQ.sort()
        self._save_collection_file_handle()

    def _save_collection_file_handle(self):
        # 一旦收藏有變動, 就儲存到收藏題目的 JSON 檔案裡
        subject = self.parameters["subject_info"]["subject"]
        year = self.parameters["test_year"]

        if os.path.exists("./_collection_question.json"):
            with open("./_collection_question.json", "r") as json_file:
                collections = load(json_file)

                # 判斷測驗科目是否的一致
                if subject not in collections.keys():
                    collections[subject] = {
                        "測驗年份": [],
                        "收藏題目": []
                    }

                if year not in collections[subject]["測驗年份"]:
                    collections[subject]["測驗年份"].append(year)
                    collections[subject]["收藏題目"].append(self.collectionQ)
                else:
                    years = collections[subject]["測驗年份"]
                    index = years.index(year)
                    collections[subject]["收藏題目"][index] = self.collectionQ

            with open("./_collection_question.json", 'w') as json_file:
                dump(collections, json_file)

        else:
            with open("./_collection_question.json", 'w') as json_file:
                data = {
                    subject: {"測驗年份": [year], "收藏題目": [self.collectionQ]}
                }
                dump(data, json_file)

    def _send_answer_event(self):
        # 到對答案的新視窗(但要把參數傳給新視窗)
        # 計算作答時間
        time_second = self.quiz_time - self.current_time
        time_min = time_second // 60
        time_second = time_second % 60

        # 交卷後的新視窗
        self.result_window = ResultWindows(
            font_size=self.parameters["font_size"],
            subject=self.parameters["subject_info"]["subject"],
            question=self.questions,
            user_answer=self.user_answers,
            answer_path=self.answers_data_path,
            test_year=self.parameters["test_year"],
            using_time=(time_min, time_second),
            first_window=self.initWindow,
            collectionQ=self.collectionQ
        )
        self.result_window.show()
        self.close()


class CollectionQWindows(QtWidgets.QWidget):
    def __init__(self, **kwargs):
        super(CollectionQWindows, self).__init__()

        # 設定視窗大小, 標題, icon, 永遠在螢幕最上層顯示
        self.width, self.height = kwargs["windows_size"][0], kwargs["windows_size"][1]
        self.setFixedSize(self.width, self.height)

        self.setWindowTitle("教師資格考試測驗系統")
        self.setWindowIcon(QtGui.QIcon("./image/windowsicon.ico"))
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        # 設定文字大小
        self.setFont(QFont('細明體', kwargs["font_size"]))

        # 初始視窗變數
        self.initWindow = kwargs["initWindow"]

        self.parameters = kwargs
        # ----- 參數設定 -----
        # - 收藏檔案的路徑
        if os.path.exists("./_collection_question.json"):
            with open("./_collection_question.json", 'r') as json_file:
                self.collection_questions = load(json_file)

            # - 題目文字, 圖片, 選項
            self.question_text = QtWidgets.QTextEdit(self)
            self.question_image = QtWidgets.QLabel(self)
            self.options_list = [QtWidgets.QLabel(self) for _ in range(4)]  # A, B, C, D

            # 設定可以快速跳轉到某一科的選單(暫時不需要)
            # self.subject_goto = QtWidgets.QComboBox(self)
            # self.page_goto = QtWidgets.QComboBox(self)

            # 設定前/後一頁的按鈕
            self.previous_btn = QtWidgets.QPushButton(self)
            self.next_btn = QtWidgets.QPushButton(self)

            # 顯示收藏圖案的 Label
            self.collection_label = QtWidgets.QLabel(self)
            self.remove_collection = list()
            self.isCollect = 1

            # 顯示題目資訊的 Label
            self.question_info = QtWidgets.QLabel(self)

            # 顯示正確答案的按鈕, Label
            self.answer_btn = QtWidgets.QPushButton(self)
            self.answer_label = QtWidgets.QLabel(self)

            # 返回首頁/離開系統的按鈕
            self.back_btn = QtWidgets.QPushButton(self)
            self.exit_btn = QtWidgets.QPushButton(self)

            # - 儲存題目資訊的所有計算變數
            self.total_questions = dict()
            self.total_answers = ["X"]
            self.subject_index = list()
            self.subject_name = list()
            self.question_number = list()
            self.current_question = 1  # 存放當前顯示的題目
            # -----

            self._handle_questions_data()
            self._windows_setting()
            self.ui()

        else:
            hint_text = QtWidgets.QLabel(self)
            hint_text.setText('目 前 暫 無 收 藏 題 目')
            hint_text.setFont(QFont('細明體', 36))
            hint_text.setGeometry(self.width // 2 - 300, self.height // 2 - 200, 600, 200)

            back_btn = QtWidgets.QPushButton(self)
            back_btn.setText('返回測驗首頁')
            back_btn.setGeometry(self.width // 2 - 240, self.height // 2, 150, 60)
            back_btn.clicked.connect(self._back_first_window)

            exit_btn = QtWidgets.QPushButton(self)
            exit_btn.setText('離開測驗系統')
            exit_btn.setGeometry(self.width // 2 + 30, self.height // 2, 150, 60)
            exit_btn.clicked.connect(self.close)

    def _windows_setting(self):
        width, height = self.width, self.height

        # 1. 設定題目文字位置
        q_text_x, q_text_w = int(width * 0.02), int(width * 0.95)
        q_text_y = int(height * 0.02)

        isImage = self.total_questions[self.current_question]["isImage"]

        if isImage == "" or isImage == "A":
            # 題目無圖片
            q_text_h = int(height * 0.5)
        else:
            # 題目有圖片
            q_text_h = int(height * 0.23)
            # 2. 設定題目圖片/表格位置
            q_img_y, q_img_h = int(height * 0.26), int(height * 0.3)
            self.question_image.setGeometry(q_text_x, q_img_y, q_text_w, q_img_h)
            self.question_image.setAlignment(QtCore.Qt.AlignLeft)

        self.question_text.setFont(QFont('細明體', self.parameters["font_size"]))
        self.question_text.setGeometry(q_text_x, q_text_y, q_text_w, q_text_h)

        palette = self.palette()
        palette.setColor(QPalette.Base, QColor(0, 0, 0, 0))
        self.question_text.setPalette(palette)

        self.question_text.setStyleSheet('''
             border: none;
         ''')
        self.question_text.setAlignment(QtCore.Qt.AlignLeft)

        # 2. 設定選項位置
        textA_y, text_w, text_h = int(height * 0.6), 20, 20
        textA_w, textA_h = int(width * 0.3), int(height * 0.18)
        self.options_list[0].setGeometry(q_text_x + text_w, textA_y, textA_w, textA_h)

        textB_x = int(width * 0.4)
        self.options_list[1].setGeometry(textB_x + text_w, textA_y, textA_w, textA_h)
        self.options_list[2].setGeometry(q_text_x + text_w, textA_y + textA_h + text_h, textA_w, textA_h)
        self.options_list[3].setGeometry(textB_x + text_w, textA_y + textA_h + text_h, textA_w, textA_h)

        for option in self.options_list:
            option.setAlignment(QtCore.Qt.AlignLeft)

        # 3. 設定上/下一題的位置
        page_btn_x = textB_x + textA_w + 4 * text_w
        page_btn_w = int(width * 0.08)
        page_btn_h = int(height * 0.05)
        self.previous_btn.setGeometry(page_btn_x, textA_y, page_btn_w, page_btn_h)
        self.next_btn.setGeometry(page_btn_x + page_btn_w + 10, textA_y, page_btn_w, page_btn_h)

        # 4. 設定收藏按鈕的位置
        pixmap2 = QtGui.QPixmap('./image/icon_yellow_star.png')
        pixmap2 = pixmap2.scaled(page_btn_h, page_btn_h)
        self.collection_label.setPixmap(pixmap2)
        self.collection_label.setGeometry(page_btn_x + page_btn_w * 2 + 20, textA_y, page_btn_h, page_btn_h)

        # 5. 顯示題目資訊位置
        q_info_w = int(width * 0.15)
        q_info_y = textA_y + int(page_btn_h * 1.2)
        self.question_info.setGeometry(page_btn_x, q_info_y, q_info_w, page_btn_h * 2)
        self.question_info.setFont(QFont('細明體', self.parameters["font_size"]))

        # 6. 顯示正確答案按鈕, Label 位置
        self.answer_btn.setGeometry(page_btn_x, q_info_y + page_btn_h * 2 + 10, int(width * 0.1), page_btn_h)
        self.answer_label.setFont(QFont('細明體', self.parameters["font_size"]))
        self.answer_label.setGeometry(page_btn_x, q_info_y + page_btn_h * 3 + 20, int(width * 0.1), page_btn_h)

        # 7. 返回首頁/離開系統的按鈕位置
        back_w = int(width * 0.1)
        self.back_btn.setGeometry(page_btn_x, q_info_y + int(page_btn_h * 5.5), back_w, page_btn_h)
        self.exit_btn.setGeometry(page_btn_x + back_w + 20, q_info_y + int(page_btn_h * 5.5), back_w, page_btn_h)

    def ui(self):
        # 設定題目文字是唯讀的
        self.question_text.setReadOnly(True)
        self._questions_setting()

        # 設定上/下一題的文字
        self.previous_btn.setText('上一題')
        self.previous_btn.clicked.connect(self._previous_question)
        self.previous_btn.setEnabled(False)
        self.next_btn.setText('下一題')
        self.next_btn.clicked.connect(self._next_question)

        # 設定收藏標籤的 label event
        self.collection_label.enterEvent = self._mouse_cursor_enter
        self.collection_label.mousePressEvent = self._collection_clicked
        self.collection_label.leaveEvent = self._mouse_cursor_leave

        # 顯示題目資訊文字
        self._show_question_info()

        # 顯示正確答案按鈕文字
        self.answer_btn.setText("顯示正確答案")
        self.answer_btn.clicked.connect(self._answers_display)

        # 返回首頁/離開系統的按鈕文字
        self.back_btn.setText('返回測驗首頁')
        self.back_btn.clicked.connect(self._back_first_window)

        self.exit_btn.setText('離開測驗系統')
        self.exit_btn.clicked.connect(self.close)

    def _mouse_cursor_enter(self, event):
        self.setCursor(QtCore.Qt.PointingHandCursor)

    def _mouse_cursor_leave(self, event):
        self.setCursor(QtCore.Qt.ArrowCursor)

    def _questions_setting(self):
        key = self.current_question
        question = self.total_questions[key]
        q, options = question["Q"]["text"], question["Option"]
        q = str(key) + '. ' + q

        if question["isImage"] == "":
            A, B, C, D = options["A"]["text"], options["B"]["text"], options["C"]["text"], options["D"]["text"]
            self.options_list[0].setText(A)
            self.options_list[1].setText(B)
            self.options_list[2].setText(C)
            self.options_list[3].setText(D)

        elif question["isImage"] == "Q":
            A, B, C, D = options["A"]["text"], options["B"]["text"], options["C"]["text"], options["D"]["text"]
            self.options_list[0].setText(A)
            self.options_list[1].setText(B)
            self.options_list[2].setText(C)
            self.options_list[3].setText(D)

            # 題目有圖片
            q_img = QPixmap(question["Q"]["img"])
            self.question_image.setPixmap(q_img)

        elif question["isImage"] == "A":
            # 選項有圖片無文字
            img_a, img_b = QPixmap(options["A"]["img"]), QPixmap(options["B"]["img"])
            img_c, img_d = QPixmap(options["C"]["img"]), QPixmap(options["D"]["img"])

            # 讓圖片 Resize 成 QLabel 的大小
            if img_a.size().width() > self.options_list[0].size().width() or \
                    img_a.size().height() > self.options_list[0].size().height():
                img_a = img_a.scaled(self.options_list[0].size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_b.size().width() > self.options_list[1].size().width() or \
                    img_b.size().height() > self.options_list[1].size().height():
                img_b = img_b.scaled(self.options_list[1].size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_c.size().width() > self.options_list[2].size().width() or \
                    img_c.size().height() > self.options_list[2].size().height():
                img_c = img_c.scaled(self.options_list[2].size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_d.size().width() > self.options_list[3].size().width() or \
                    img_d.size().height() > self.options_list[3].size().height():
                img_d = img_d.scaled(self.options_list[3].size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            self.options_list[0].setPixmap(img_a)
            self.options_list[1].setPixmap(img_b)
            self.options_list[2].setPixmap(img_c)
            self.options_list[3].setPixmap(img_d)

        else:
            # 題目 & 選項都有圖片
            q_img = QPixmap(question["Q"]["img"])
            self.question_image.setPixmap(q_img)

            img_a, img_b = QPixmap(options["A"]["img"]), QPixmap(options["B"]["img"])
            img_c, img_d = QPixmap(options["C"]["img"]), QPixmap(options["D"]["img"])

            # 讓圖片 Resize 成 QLabel 的大小
            if img_a.size().width() > self.options_list[0].size().width() or \
                    img_a.size().height() > self.options_list[0].size().height():
                img_a = img_a.scaled(self.options_list[0].size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_b.size().width() > self.options_list[1].size().width() or \
                    img_b.size().height() > self.options_list[1].size().height():
                img_b = img_b.scaled(self.options_list[1].size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_c.size().width() > self.options_list[2].size().width() or \
                    img_c.size().height() > self.options_list[2].size().height():
                img_c = img_c.scaled(self.options_list[2].size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_d.size().width() > self.options_list[3].size().width() or \
                    img_d.size().height() > self.options_list[3].size().height():
                img_d = img_d.scaled(self.options_list[3].size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            self.options_list[0].setPixmap(img_a)
            self.options_list[1].setPixmap(img_b)
            self.options_list[2].setPixmap(img_c)
            self.options_list[3].setPixmap(img_d)

        self.question_text.setText(q)

    def _show_question_info(self):
        subject_name, subject_index, question_number = self.subject_name, self.subject_index, self.question_number
        current_question = self.current_question
        index = 0

        for i, number_bound in enumerate(subject_index):
            if current_question < number_bound:
                index = i
                break

        subject, year = subject_name[index]
        number = question_number[current_question - 1]
        self.question_info.setText("科目：" + subject + "\n" + "題目年份：" + year + "\n題號：" + str(number))

    def _update_btn_state(self):
        if self.current_question == 1:
            self.previous_btn.setEnabled(False)
        else:
            self.previous_btn.setEnabled(True)

        if self.current_question >= self.subject_index[-1] - 1:
            self.next_btn.setEnabled(False)
        else:
            self.next_btn.setEnabled(True)

    def _update_question_image_state(self):
        # 更新題目圖片的狀態 question_image 的 state
        key = self.current_question
        question = self.total_questions[key]["Q"]
        if question["img"] == '':
            self.question_image.clear()

    def _collection_clicked(self, event):
        # 將已收藏的題目取消/或更改狀態, 但要在下次進入系統時再消除
        text = self.question_info.text().split("\n")
        subject, year, number = text
        subject = subject.split("：")[-1]
        year = year.split("：")[-1]
        number = int(number.split("：")[-1])

        if [subject, year, number] not in self.remove_collection:
            self.remove_collection.append([subject, year, number])

        h = int(self.height * 0.05)
        if self.isCollect:
            self.isCollect = 0
            pixmap = QtGui.QPixmap('./image/icon_black_star.png')
        else:
            self.isCollect = 1
            pixmap = QtGui.QPixmap('./image/icon_yellow_star.png')
            self.remove_collection.remove([subject, year, number])

        pixmap = pixmap.scaled(h, h)
        self.collection_label.setPixmap(pixmap)

    def _restore_collection_mark(self):
        # 恢復收藏按鈕的標記
        text = self.question_info.text().split("\n")
        subject, year, number = text
        subject = subject.split("：")[-1]
        year = year.split("：")[-1]
        number = int(number.split("：")[-1])

        h = int(self.height * 0.05)
        if [subject, year, number] in self.remove_collection:
            self.isCollect = 0
            pixmap = QtGui.QPixmap('./image/icon_black_star.png')
        else:
            self.isCollect = 1
            pixmap = QtGui.QPixmap('./image/icon_yellow_star.png')

        pixmap = pixmap.scaled(h, h)
        self.collection_label.setPixmap(pixmap)

    def _previous_question(self):
        self.current_question -= 1

        self._update_btn_state()
        self._windows_setting()
        self._questions_setting()
        self._show_question_info()
        self._restore_collection_mark()
        self._update_question_image_state()
        self._clear_answer_display()

    def _next_question(self):
        self.current_question += 1

        self._update_btn_state()
        self._windows_setting()
        self._questions_setting()
        self._show_question_info()
        self._restore_collection_mark()
        self._update_question_image_state()
        self._clear_answer_display()

    def _clear_answer_display(self):
        self.answer_label.clear()

    def _answers_display(self):
        answer = self.total_answers[self.current_question]
        self.answer_label.setText("正確答案： " + answer)

    def _handle_questions_data(self):
        q_files = {
            "國語文能力測驗": chineseQ.YEARS,
            "數學能力測驗": mathQ.YEARS,
            "教育理念與實務": esprQ.YEARS,
            "課程教學與評量": escntQ.YEARS,
            "學習者發展與適性輔導": esdngQ.YEARS
        }

        answers_path = {
            "國語文能力測驗": "./Answer/ChineseA.json",
            "數學能力測驗": "./Answer/MathA.json",
            "教育理念與實務": "./Answer/EsprA.json",
            "課程教學與評量": "./Answer/EscntA.json",
            "學習者發展與適性輔導": "./Answer/EsdngA.json"
        }

        questions = self.collection_questions
        subjects = questions.keys()

        subject_index = self.subject_index  # 存放當前 subject 和 year 的題數(用累加的做法)
        subject_name = self.subject_name
        question_number = self.question_number
        currentNumber = 1

        for index, subject in enumerate(subjects):
            year_list, questions_list = questions[subject]["測驗年份"], questions[subject]["收藏題目"]

            # 處理答案, 題目資訊
            answers_file = load(open(answers_path[subject]))
            for i, year in enumerate(year_list):
                questions_list[i].sort()  # 預防出現題目 & 答案對不起來的問題
                subject_name.append([subject, year])  # 顯示題目資訊需要

                for number in questions_list[i]:
                    self.total_answers.append(answers_file[year][number - 1])

            # 利用 index 去找到相對應的題目(處理 108 年有 2 份的問題)
            if '108-2' in year_list:
                year_list[year_list.index('108-2')] = '108'
            if '108-1' in year_list:
                year_list[year_list.index('108-1')] = '107'

            # 呼叫對應的 function
            year_index = [112 - int(i) for i in year_list]

            for q_index, y_index in enumerate(year_index):
                target_question = q_files[subject][y_index]
                target_number = questions_list[q_index]
                target_number.sort()

                for number in target_number:
                    self.total_questions[currentNumber] = target_question[number]
                    currentNumber += 1
                    question_number.append(number)
                subject_index.append(currentNumber)

    def _back_first_window(self):
        self.initWindow.show()
        self.close()


class ResultWindows(QtWidgets.QWidget):
    def __init__(self, **kwargs):
        super(ResultWindows, self).__init__()

        self.setWindowTitle("教師資格考試測驗系統")
        self.setWindowIcon(QtGui.QIcon("./image/windowsicon.ico"))
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.setFont(QFont('細明體', kwargs["font_size"]))
        self.setFixedSize(1920, 900)

        self.parameters = kwargs

        # ----- 參數設定 -----
        # -- 版面布局設定 --
        self.window_layout = QtWidgets.QGridLayout(self)
        # - 顯示正確答案 & 使用者答案的 layout
        self.labels_layout = QtWidgets.QGridLayout(self)
        # - 顯示問題, 圖片的 layout
        self.question_layout = QtWidgets.QGridLayout(self)
        # - 顯示選項的 layout
        self.options_layout = QtWidgets.QGridLayout(self)
        # - 顯示按鈕的 layout
        self.button_layout = QtWidgets.QHBoxLayout(self)
        # --

        # 設定標題, 說明, 正確率標籤, 儲存本次測驗的按鈕
        self.title_label = QtWidgets.QLabel(self)
        self.illustrate_label = QtWidgets.QLabel(self)
        self.accuracy_label = QtWidgets.QLabel(self)
        self.save_test_btn = QtWidgets.QPushButton(self)

        # 設定顯示題號, 使用者選項, 正確答案的標籤
        self.question_number = len(kwargs["question"].keys())
        self.labels_list = list()
        for i in range(0, self.question_number):
            label = QtWidgets.QLabel(self)
            self.labels_list.append(label)

        # 設定顯示題目, 圖片, 選項的元件
        self.question_text = QtWidgets.QTextEdit(self)
        self.question_image = QtWidgets.QLabel(self)
        self.optionA, self.optionB = QtWidgets.QLabel(self), QtWidgets.QLabel(self)
        self.optionC, self.optionD = QtWidgets.QLabel(self), QtWidgets.QLabel(self)

        # 設定按鈕元件
        self.back_first_window_btn = QtWidgets.QPushButton(self)
        self.history_btn = QtWidgets.QPushButton(self)
        self.exit_system = QtWidgets.QPushButton(self)

        # - 儲存收藏題目
        self.collectionQ = kwargs["collectionQ"]

        # - 批改答案相關變數
        self.question = kwargs["question"]
        self.year = kwargs["test_year"]
        self.user_answer = kwargs["user_answer"]
        self.answer_path = kwargs["answer_path"]
        self.correct = 0
        self.wrong_number = list()
        self.current_number = 1
        # -----

        self._windows_setting()
        self.ui()
        pass

    def _windows_setting(self):
        # 視窗大小的基本設定
        width, height = self.width(), self.height()

        # 讓視窗在螢幕正中間顯示
        screen = QtWidgets.QApplication.desktop()
        screen_width, screen_height = screen.width(), screen.height()
        self.move((screen_width - width) // 2, (screen_height - height) // 2)

        # - 處理 labels_layout
        # 1. 設定 title label 文字, 樣式
        reducing_time = self.parameters["using_time"]
        minute = str(reducing_time[0])
        second = '0' + str(reducing_time[1]) if reducing_time[1] < 10 else str(reducing_time[1])
        subject = self.parameters["subject"]

        self.title_label.setText(f'測驗科目：{subject}\n作答時間：{minute}分{second}秒')
        self.title_label.setAlignment(QtCore.Qt.AlignLeft)

        label_list = self.labels_list
        last_row = len(label_list) // 10 if len(label_list) % 10 == 0 else len(label_list) // 10 + 1
        self.labels_layout.addWidget(self.title_label, 0, 0, 1, last_row)

        # 2. 設定 illustrate label 文字, 樣式
        html_illustrate = '''
        <font color="black">使用者答案是</font>
        <font color="blue">藍色文字</font>
        <br/>
        <font color="black">正確答案是</font>
        <font color="red">紅色文字</font>'''
        self.illustrate_label.setText(html_illustrate)
        self.illustrate_label.setFont(QFont('細明體', self.parameters["font_size"]))
        self.illustrate_label.setStyleSheet('''border: solid black; border-width: 0px 0px 1px 0px;''')
        self.labels_layout.addWidget(self.illustrate_label, 12, 0, 1, last_row)

        self.labels_layout.addWidget(self.accuracy_label, 13, 0, 1, last_row)

        self.save_test_btn.setText('儲存本次測驗')
        self.labels_layout.addWidget(self.save_test_btn, 13, last_row - 1)

        # - 處理 button_layout 文字, 樣式
        self.back_first_window_btn.setText('返回測驗首頁')
        self.button_layout.addWidget(self.back_first_window_btn, 0)

        self.history_btn.setText('歷史測驗紀錄')
        self.button_layout.addWidget(self.history_btn, 0)

        self.exit_system.setText('離開測驗')
        self.button_layout.addWidget(self.exit_system, 0)
        # -

        # - 處理 question_layout 的文字, 樣式
        text_width = int(width * 0.6)

        isImage = self.question[self.current_number]["isImage"]
        if isImage == "" or isImage == "A":
            text_height = int(height * 0.4)
        else:
            text_height = int(height * 0.25)

            self.question_image.setAlignment(QtCore.Qt.AlignCenter)
            self.question_layout.addWidget(self.question_image, 1, 0)

        self.question_layout.addWidget(self.question_text, 0, 0)
        self.question_text.setFixedSize(text_width, text_height)

        self.question_text.setFont(QFont('細明體', self.parameters["font_size"]))
        self.question_text.setStyleSheet('''border: none;''')
        palette = self.palette()
        palette.setColor(QPalette.Base, QColor(0, 0, 0, 0))
        self.question_text.setPalette(palette)

        self.options_layout.addWidget(self.optionA, 0, 0)
        self.options_layout.addWidget(self.optionB, 0, 1)
        self.options_layout.addWidget(self.optionC, 1, 0)
        self.options_layout.addWidget(self.optionD, 1, 1)

        self.question_layout.addLayout(self.options_layout, 2, 0)

        self.window_layout.addLayout(self.labels_layout, 0, 0, 2, 1)
        self.window_layout.addLayout(self.question_layout, 0, 1)
        self.window_layout.addLayout(self.button_layout, 1, 1)

    def ui(self):
        label_list = self.labels_list

        for i, label in enumerate(label_list):
            column, row = i % 10, i // 10
            label.setStyleSheet('''border: 1px solid;''')  # 同時設定答案框的樣式
            self.labels_layout.addWidget(label, column + 1, row)

            # label 相關滑鼠事件設定
            label.enterEvent = self._mouse_cursor_enter
            label.leaveEvent = self._mouse_cursor_leave
            label.mousePressEvent = lambda event, clicked_label=label: self._question_is_clicked(event, clicked_label)

        self._correct_answer_event()

        # 處理 back_first_window_btn 事件
        self.back_first_window_btn.clicked.connect(self._back_first_window)
        self.exit_system.clicked.connect(self._exit_system)

        # 設定 question text Read Only
        self.question_text.setReadOnly(True)

        # 儲存本次測驗按鈕事件設定
        self.save_test_btn.clicked.connect(self._save_current_test)

        # 查看歷史紀錄
        self.history_btn.clicked.connect(self._history_test_show)
        pass

    def _save_current_test(self):
        # 將測驗科目, 作答時間, 日期, 時間, 正確率, 錯誤題數儲存起來(用 JSON 檔案)
        subject, using_time = self.title_label.text().split('\n')
        subject, using_time = subject.split('：')[1], using_time.split('：')[1]

        today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        acc_number, acc_percent = self.accuracy_label.text().split('\n')
        acc_number, acc_percent = acc_number.split('：')[1], acc_percent.split('：')[1]

        wrong_number = [str(i) for i in self.wrong_number]
        wrong_number = ' '.join(wrong_number)

        data_test = {
            "測驗日期": today,
            "測驗科目": subject,
            "測驗年分": self.year,
            "作答時間": using_time,
            "正確題數": acc_number,
            "正確率": acc_percent,
            "錯誤題號": wrong_number
        }

        # 若路徑已經有檔案了, 則先讀取先前的資料後再複寫
        if os.path.exists("./_history_test.json"):
            history = open("./_history_test.json")
            old_data = load(history)

            # 最多保留最新的 20 筆測驗紀錄
            data_number = len(old_data.keys())
            if data_number == 20:
                for i in range(1, 20):
                    old_data[str(i)] = old_data[str(i + 1)]
                old_data["20"] = data_test
            else:
                old_data[str(data_number + 1)] = data_test

            with open("./_history_test.json", 'w') as history:
                dump(old_data, history, indent=4)

        else:
            with open("./_history_test.json", 'w') as history:
                data_test = {"1": data_test}
                dump(data_test, history, indent=4)

        # 儲存過一次之後就將按鈕設置成不能再按的狀態
        self.save_test_btn.setEnabled(False)

    def _mouse_cursor_enter(self, event):
        self.setCursor(QtCore.Qt.PointingHandCursor)

    def _mouse_cursor_leave(self, event):
        self.setCursor(QtCore.Qt.ArrowCursor)

    def _update_question_image_state(self, number):
        # 更新題目圖片的狀態 question_image 的 state
        question = self.question[int(number)]["Q"]
        if question["img"] == '':
            self.question_image.clear()

    def _question_is_clicked(self, event, clicked_label):
        html_text = clicked_label.text()  # 取得 HTML 的文本
        number = html_text.split('.')[0].split('>')[-1]  # 取得題號

        self.current_number = int(number)  # 用給 ui() 調整版面使用
        self._windows_setting()
        self._update_question_image_state(number)
        self._display_clicked_question(number)

    def _display_clicked_question(self, number):
        question = self.question[int(number)]
        q, options = question['Q']["text"], question["Option"]
        q = str(number) + ". " + q

        if question["isImage"] == "":
            A, B, C, D = options["A"]["text"], options["B"]["text"], options["C"]["text"], options["D"]["text"]
            self.optionA.setText(A)
            self.optionB.setText(B)
            self.optionC.setText(C)
            self.optionD.setText(D)

        elif question["isImage"] == "Q":
            A, B, C, D = options["A"]["text"], options["B"]["text"], options["C"]["text"], options["D"]["text"]
            self.optionA.setText(A)
            self.optionB.setText(B)
            self.optionC.setText(C)
            self.optionD.setText(D)

            # 題目有圖片
            q_img = QPixmap(question["Q"]["img"])
            self.question_image.setPixmap(q_img)

        elif question["isImage"] == "A":
            # 選項有圖片無文字
            img_a = QPixmap(options["A"]["img"])
            img_b = QPixmap(options["B"]["img"])
            img_c = QPixmap(options["C"]["img"])
            img_d = QPixmap(options["D"]["img"])

            if img_a.size().width() > self.optionA.size().width() or \
                    img_a.size().height() > self.optionA.size().height():
                img_a = img_a.scaled(self.optionA.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_b.size().width() > self.optionB.size().width() or \
                    img_b.size().height() > self.optionB.size().height():
                img_b = img_b.scaled(self.optionB.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_c.size().width() > self.optionC.size().width() or \
                    img_c.size().height() > self.optionC.size().height():
                img_c = img_c.scaled(self.optionC.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_d.size().width() > self.optionD.size().width() or \
                    img_d.size().height() > self.optionD.size().height():
                img_d = img_d.scaled(self.optionD.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            self.optionA.setPixmap(img_a)
            self.optionB.setPixmap(img_b)
            self.optionC.setPixmap(img_c)
            self.optionD.setPixmap(img_d)

        else:
            # 題目和答案都有圖片
            q_img = QPixmap(question["Q"]["img"])
            self.question_image.setPixmap(q_img)

            img_a, img_b = QPixmap(options["A"]["img"]), QPixmap(options["B"]["img"])
            img_c, img_d = QPixmap(options["C"]["img"]), QPixmap(options["D"]["img"])

            if img_a.size().width() > self.optionA.size().width() or \
                    img_a.size().height() > self.optionA.size().height():
                img_a = img_a.scaled(self.optionA.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_b.size().width() > self.optionB.size().width() or \
                    img_b.size().height() > self.optionB.size().height():
                img_b = img_b.scaled(self.optionB.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_c.size().width() > self.optionC.size().width() or \
                    img_c.size().height() > self.optionC.size().height():
                img_c = img_c.scaled(self.optionC.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            if img_d.size().width() > self.optionD.size().width() or \
                    img_d.size().height() > self.optionD.size().height():
                img_d = img_d.scaled(self.optionD.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            self.optionA.setPixmap(img_a)
            self.optionB.setPixmap(img_b)
            self.optionC.setPixmap(img_c)
            self.optionD.setPixmap(img_d)

        self.question_text.setText(q)

    def _correct_answer_event(self):
        with open(self.answer_path) as answer_data:
            json = load(answer_data)
            current_year_answer = json[self.year]

        # 將使用者的答案, 轉換成 A, B, C, D
        user_answer = self.user_answer
        for i, ans in enumerate(user_answer):
            option = chr(ans + 64) if ans != 0 else '&nbsp;'  # HTML 的空格顯示
            user_answer[i] = option

        # 若使用者答案正確就不要顯示解答的答案
        correct = self.correct
        wrong_number = self.wrong_number  # 儲存錯誤答案的題號
        for index, user_ans in enumerate(user_answer):
            question_number = str(index + 1) + '. '
            if user_ans != current_year_answer[index]:
                html_text_setting = f'''
                <font color="black">{question_number}</font>
                <font color="blue">{user_ans}</font>
                <font color="red">{current_year_answer[index]}</font>'''
                wrong_number.append(index + 1)

                if index + 1 not in self.collectionQ:
                    self.collectionQ.append(index + 1)

            else:
                html_text_setting = f'''
                <font color="black">{question_number}</font>
                <font color="blue">{user_ans}</font>
                '''
                correct += 1

            self.labels_list[index].setText(html_text_setting)

        self.correct = correct

        # 顯示正確題數
        accuracy = "{:.2f}".format(correct * 100 / len(user_answer))
        self.accuracy_label.setText(f'正確題數/總共題數：{correct}/{len(user_answer)}\n正確率：{accuracy}%')

        # - 將錯誤題目儲存到收藏題目裡面
        self._save_collection_file_handle()

    def _save_collection_file_handle(self):
        subject = self.parameters["subject"]
        year = self.year

        if os.path.exists("./_collection_question.json"):
            with open("./_collection_question.json", "r") as json_file:
                collections = load(json_file)

                # 判斷測驗科目是否的一致
                if subject not in collections.keys():
                    collections[subject] = {
                        "測驗年份": [],
                        "收藏題目": []
                    }

                if year not in collections[subject]["測驗年份"]:
                    collections[subject]["測驗年份"].append(year)
                    collections[subject]["收藏題目"].append(self.collectionQ)
                else:
                    years = collections[subject]["測驗年份"]
                    index = years.index(year)
                    collections[subject]["收藏題目"][index] = self.collectionQ

            with open("./_collection_question.json", 'w') as json_file:
                dump(collections, json_file)

        else:
            with open("./_collection_question.json", 'w') as json_file:
                data = {
                    subject: {"測驗年份": [year], "收藏題目": [self.collectionQ]}
                }
                dump(data, json_file)

    def _back_first_window(self):
        self.parameters["first_window"].show()
        self.close()

    def _history_test_show(self):
        self.history_window = HistoryWindow()
        self.history_window.show()

    def _exit_system(self):
        self.close()


class HistoryWindow(QtWidgets.QWidget):
    def __init__(self):
        super(HistoryWindow, self).__init__()

        self.setWindowTitle("教師資格考試測驗系統")
        self.setWindowIcon(QtGui.QIcon("./image/windowsicon.ico"))
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        # 顯示歷史紀錄的標籤
        self.history_table = QtWidgets.QTableWidget(self)

        self._windows_setting()
        self.ui()

    def _windows_setting(self):
        self.setFixedSize(900, 720)
        x, y, w, h = 10, 10, 880, 700
        self.history_table.verticalHeader().setMinimumWidth(20)

        # 設定表格的相關資訊
        self.history_table.setColumnCount(7)
        self.history_table.setHorizontalHeaderLabels(
            ['測驗日期', '測驗科目', '測驗年份', '作答時間', '正確題數', '正確率', '錯誤題號']
        )

        self.history_table.setFont(QFont('新細明體', 10))
        self.history_table.setGeometry(x, y, w, h)

        self.history_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.history_table.setStyleSheet('''
            border: 1px solid black;
        ''')

    def ui(self):
        # 顯示測驗的歷史紀錄
        if os.path.exists("./_history_test.json"):
            with open("./_history_test.json") as history:
                database = load(history)
                self.history_table.setRowCount(len(database.keys()))

                for i, count in enumerate(database.keys()):
                    for j, data in enumerate(database[count].values()):
                        data = QtWidgets.QTableWidgetItem(str(data))  # 要轉換成 pyqt5 表格專用的字串
                        self.history_table.setItem(i, j, data)
        else:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = InitialWindow()
    window.show()
    sys.exit(app.exec_())
