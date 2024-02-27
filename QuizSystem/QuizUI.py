from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QFont, QPalette, QColor
from json import load
import sys

# 可以根據使用者選的選項之後, 再 import 特定的檔案和答案
import Question.Chinese.ChineseQ as chineseQ
import Question.Math.MathQ as mathQ
import Question.Espr.EsprQ as esprQ
import Question.Esdng.EsdngQ as esdngQ
import Question.Escnt.EscntQ as escntQ


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
        self.setFixedSize(1200, 768)

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

        # 設定 Message Box 變數
        self.test_msgbox = QtWidgets.QMessageBox(self)

        # 新視窗的變數
        self.quiz_windows = None
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

        self.description.setFont(ch_font)
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

        # 9. 顯示測驗考卷資訊的位置
        test_info_y = int(self.height() * 0.7)
        test_info_w = int(subject_x * 3 // 5)
        self.test_info.setGeometry(subject_x, test_info_y, test_info_w, self.height() - test_info_y)
        self.test_info.setFont(QFont('標楷體', 13))

        # 10. 設定 QMessageBox 位置
        self.test_msgbox.setStyleSheet('''font-size: 16px;''')

    def ui(self):
        # 設定初始畫面的標題
        self.init_title.setText('教  檢  歷  屆  試  題  測  驗  系  統')

        # windows size select
        self.label_size.setText('選擇視窗大小：')
        self.median.setChecked(True)
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
3. 在選擇範圍中, 選擇想測驗的試卷年份\n4. 確定選擇正確後, 點選進入測驗的按鈕\n5. 再次確認考試資訊無誤後, 點選確認進入正式測驗\n\n版本說明：\n''')
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

        # 新增自訂義按鈕
        sure = QtWidgets.QPushButton("確定")
        cancel = QtWidgets.QPushButton("取消")
        self.test_msgbox.addButton(sure, QtWidgets.QMessageBox.AcceptRole)
        self.test_msgbox.addButton(cancel, QtWidgets.QMessageBox.RejectRole)

        self.enter_test_btn.clicked.connect(self._enter_test_event)

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
        if select_id == 1:
            lst = [str(i) for i in range(103, 113)]
        else:
            lst = [str(i) for i in range(94, 113)]
            # lst.append("103 ~ 112")

        lst.insert(0, "請選擇年份")
        # lst.append("94 ~ 102")  # 複數考題功能以後新增
        # lst.append("全選")

        # 去除 107 題目, 和區分 108 年兩份試卷
        lst[lst.index('107')] = '108-1'
        lst[lst.index('108')] = '108-2'

        self.years_menu.clear()  # 要清除先前的下拉式選單選項, 才不會一直疊加
        self.years_menu.addItems(lst)
        self.years_menu.currentIndexChanged.connect(self._year_select_event)

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
            self.hide()
            self.quiz_windows.show()


class QuizWindows(QtWidgets.QWidget):
    def __init__(self, **kwargs):
        super(QuizWindows, self).__init__()

        self.setWindowTitle("教師資格考試測驗系統")
        self.setWindowIcon(QtGui.QIcon("./image/windowsicon.ico"))
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        # 初始視窗的參數
        self.parameters = kwargs
        self.setFont(QFont('細明體', kwargs["font_size"]))

        # -- 初始視窗
        # self.initWindow = kwargs["initWindow"]

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

        # 交卷的變數
        self.send_answer_btn = QtWidgets.QPushButton(self)
        self.result_window = None  # 新視窗的變數
        # -----

        self._window_setting()
        self.ui()

    def _window_setting(self):
        # 設定視窗大小並固定在螢幕正中間出現
        windows = self.parameters['windows_size']
        width, height = windows
        self.setFixedSize(width, height)

        screen = QtWidgets.QApplication.desktop()
        screen_width, screen_height = screen.width(), screen.height()
        self.move((screen_width - width) // 2, (screen_height - height) // 2)

        # @@ 所有元件會因為該題目/選項中是否有圖片去調整位置, 下面先設定無圖片版本的
        # 1. 設定題目文字位置
        # !! 先設定固定值, 若題目或選項中有圖片時, 再更改大小(以下的設定是 question, option 都有圖片的設定)
        q_text_x, q_text_w = int(width * 0.02), int(width * 0.95)
        q_text_y, q_text_h = int(height * 0.02), int(height * 0.23)
        self.question_text.setGeometry(q_text_x, q_text_y, q_text_w, q_text_h)

        palette = self.palette()
        palette.setColor(QPalette.Base, QColor(0, 0, 0, 0))
        self.question_text.setPalette(palette)

        self.question_text.setStyleSheet('''
            border: none;
        ''')
        self.question_text.setAlignment(QtCore.Qt.AlignLeft)

        # 2. 設定題目圖片/表格位置
        q_img_y, q_img_h = int(height * 0.26), int(height * 0.3)
        self.question_image.setGeometry(q_text_x, q_img_y, q_text_w, q_img_h)
        self.question_image.setAlignment(QtCore.Qt.AlignCenter)

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
        pass

        # 7. 交卷按鈕位置
        send_btn_x, send_btn_y = page_btn_x + page_btn_w + 10, page_goto_y + page_btn_h * 5
        send_btn_w, send_btn_h = int(width * 0.1), int(height * 0.05)
        self.send_answer_btn.setFont(QFont('細明體', 14))
        self.send_answer_btn.setGeometry(send_btn_x, send_btn_y, send_btn_w, send_btn_h)

    def ui(self):
        # 設定 question_text & image 內容(未來要抓題目的資料)
        self.question_text.setReadOnly(True)
        self._questions_setting()

        # img_example = QtGui.QImage('img_exam.PNG')
        # self.question_image.setPixmap(QtGui.QPixmap.fromImage(img_example))

        # 設定 option btn A, B, C, D
        self.option_group.addButton(self.btn_A, id=1)
        self.option_group.addButton(self.btn_B, id=2)
        self.option_group.addButton(self.btn_C, id=3)
        self.option_group.addButton(self.btn_D, id=4)

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

        # 設定交卷按鈕
        self.send_answer_btn.setText('交卷')
        self.send_answer_btn.clicked.connect(self._timer_pause)

    def _questions_setting(self):
        key = self.current_question
        question = self.questions[key]

        if question["isImage"] == "":
            q, options = question["Q"]["text"], question["Option"]
            A, B, C, D = options["A"]["text"], options["B"]["text"], options["C"]["text"], options["D"]["text"]

            q = str(key) + '. ' + q

            self.question_text.setText(q)
            self.text_A.setText(A)
            self.text_B.setText(B)
            self.text_C.setText(C)
            self.text_D.setText(D)

        elif question["isImage"] == "Q":
            # 題目有圖片
            pass

        elif question["isImage"] == "A":
            # 選項有圖片
            pass
        elif question["isImage"] == "Q&A":
            # 題目 & 選項都有圖片
            pass
        pass

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
        self._questions_setting()

    def _next_question(self):
        self.current_question += 1
        self._update_btn_state()
        self._restore_option_choice()
        self._questions_setting()

    def _page_goto_event(self):
        self.current_question = self.page_goto.currentIndex()
        self._update_btn_state()
        self._restore_option_choice()
        self._questions_setting()

    def _timer_count(self):
        minute = str(self.current_time // 60)
        if self.current_time % 60 < 10:
            second = '0' + str(self.current_time % 60)
        else:
            second = str(self.current_time % 60)

        self.timer_label.setText(f'剩餘時間：{minute}分{second}秒')
        self.current_time = self.current_time - 1
        pass

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

    def _correct_answer_event(self):
        """使用者點交卷之後, 就會開始對答案, 且會在新的視窗呈現結果"""

        with open(self.answers_data_path) as answer_data:
            json = load(answer_data)
            current_year_answer = json[self.parameters["test_year"]]

        user_answer = self.user_answers
        answer_lst = [ord(i) - 64 for i in current_year_answer]
        pass

    def _send_answer_event(self):
        # 到對答案的新視窗(但要把參數傳給新視窗)
        # 交卷後的新視窗
        self.result_window = ResultWindows(
            window_size=(self.width(), self.height()),
            font_size=self.parameters["font_size"],
            questions=self.questions,
            user_answer=self.user_answers,
            answer_path=self.answers_data_path
        )
        # self.hide()
        self.result_window.show()
        pass
    pass


class ResultWindows(QtWidgets.QWidget):
    def __init__(self, **kwargs):
        super(ResultWindows, self).__init__()

        self.setWindowTitle("教師資格考試測驗系統")
        self.setWindowIcon(QtGui.QIcon("./image/windowsicon.ico"))
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.setFont(QFont('細明體', kwargs["font_size"]))

        self.parameters = kwargs

        # ----- 參數設定 -----
        # -- 版面布局設定 --
        self.window_layout = QtWidgets.QGridLayout(self)
        # - 顯示正確答案 & 使用者答案的 layout
        self.labels_layout = QtWidgets.QGridLayout(self)
        # - 顯示問題, 選項, 圖片的 layout
        self.question_layout = QtWidgets.QGridLayout(self)
        # - 顯示按鈕的 layout
        self.button_layout = QtWidgets.QHBoxLayout(self)
        # --

        # 設定說明, 正確率標籤, 儲存本次測驗的按鈕
        self.illustrate_label = QtWidgets.QLabel(self)
        self.accuracy_label = QtWidgets.QLabel(self)
        self.save_test_btn = QtWidgets.QPushButton(self)

        # 設定顯示題號, 使用者選項, 正確答案的標籤
        self.question_number = len(kwargs["questions"].keys())
        self.labels_list = list()
        for i in range(0, self.question_number):
            label = QtWidgets.QLabel(self)
            self.labels_list.append(label)

        # 設定顯示題目, 圖片, 選項的元件
        self.question_text = QtWidgets.QTextEdit(self)
        self.question_image = QtWidgets.QLabel(self)
        self.options = QtWidgets.QLabel(self)

        # 設定按鈕元件
        self.back_first_window_btn = QtWidgets.QPushButton(self)
        self.history_btn = QtWidgets.QPushButton(self)
        self.exit_system = QtWidgets.QPushButton(self)
        # -----

        self._windows_setting()
        self.ui()
        pass

    def _windows_setting(self):
        width, height = self.parameters["window_size"][0], self.parameters["window_size"][1]
        self.setFixedSize(width, height)

        self.illustrate_label.setStyleSheet('''border: 1px solid;''')
        self.accuracy_label.setStyleSheet('''border: 1px solid;''')

        text_width, text_height = int(width * 0.5), int(height * 0.3)
        self.question_text.setFixedSize(text_width, text_height)

        self.question_text.setStyleSheet('''border: 1px solid;''')
        self.question_layout.addWidget(self.question_text, 0, 0)

        self.question_image.setText('這是要放 image 的 label')
        self.question_image.setStyleSheet('''border: 1px solid;''')
        self.question_layout.addWidget(self.question_image, 1, 0)

        self.options.setText('這是放 4 個選項的 label')
        self.options.setStyleSheet('''border: 1px solid;''')
        self.question_layout.addWidget(self.options, 2, 0)

        self.window_layout.addLayout(self.labels_layout, 0, 0, 2, 1)
        self.window_layout.addLayout(self.question_layout, 0, 1)
        self.window_layout.addLayout(self.button_layout, 1, 1)
        pass

    def ui(self):
        label_list = self.labels_list

        for i, label in enumerate(label_list):
            column, row = i % 10, i // 10
            label.setText(f'{str(i + 1)}. ')
            label.setStyleSheet('''border: 1px solid;''')
            self.labels_layout.addWidget(label, column + 1, row)

        last_row = len(label_list) // 10 if len(label_list) % 10 == 0 else len(label_list) // 10 + 1

        self.illustrate_label.setText('這是 illustrate label')
        self.labels_layout.addWidget(self.illustrate_label, 0, 0, 1, last_row)

        self.accuracy_label.setText('這是 Accuracy label')
        self.labels_layout.addWidget(self.accuracy_label, 12, 0, 1, last_row)

        self.save_test_btn.setText('儲存本次測驗')
        self.labels_layout.addWidget(self.save_test_btn, 12, last_row - 1)

        self.back_first_window_btn.setText('返回測驗首頁')
        self.button_layout.addWidget(self.back_first_window_btn, 0)

        self.history_btn.setText('歷史測驗紀錄')
        self.button_layout.addWidget(self.history_btn, 0)

        self.exit_system.setText('離開測驗')
        self.button_layout.addWidget(self.exit_system, 0)

        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = InitialWindow()
    window.show()
    sys.exit(app.exec_())
