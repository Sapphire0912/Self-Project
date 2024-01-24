# DesktopPet v1.0 設計
# 設計目標皆在 DesktopPet Design.docx 裡面
# 這裡主要需說明實現的步驟

import os
import sys
import numpy as np

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLabel, QGraphicsOpacityEffect, QComboBox, \
    QDesktopWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap, QCursor, QFont, QIcon
from PyQt5.QtCore import Qt


class DesktopPet(QMainWindow):
    def __init__(self):
        super(DesktopPet, self).__init__()

        # --- attribute setting ---
        self.style = '''
        background:%s;
        font:%spx %s;
        border-radius:%spx;
        '''
        self.characterList = [
            '珊瑚宮心海',
            '達達利亞',
            '克拉拉'
        ]
        self.charNameList = [
            'kokomi',
            'tartaglia',
            'clala'
        ]
        self.TargetPet = None  # 開啟新視窗的時候需要的暫存變數, 否則新視窗會直接結束應用程式

        # - initLogUI() 屬性 & 變數
        self.enter_bg = None
        self.logText = None
        self.stateLabel = None
        self.stateLabel2 = None
        self.hintText = None
        self.opacity_effect = QGraphicsOpacityEffect(self)  # 調整透明度
        self.opacity_effect2 = QGraphicsOpacityEffect(self)
        self.selectBox = None
        self.sureBtn = None
        self.exitBtn = None

        # - initPetImage() 屬性 & 變數
        self.character = -1

        # --- 執行 class method ---
        self.initLogUI()  # 設定執行應用程式時的 UI 介面

    def initLogUI(self):
        """
        initLogUI(self): 設定執行應用程式後所顯示的介面, 並且可以選擇要使用哪隻寵物
        """
        # ----- UI 基本設計 -----
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setGeometry(0, 0, 1600, 1200)
        self.repaint()
        # End.

        # ----- 設定視窗文字 & 背景, 按鈕元件, 下拉式選單 -----
        self.enter_bg = QLabel(self)
        self.enter_bg.setGeometry(320, 270, 850, 550)
        self.enter_bg.setPixmap(QPixmap("./background/v1_0_kokomiNamecard.png"))

        self.logText = QLabel(self)
        self.logText.setGeometry(180, 200, 800, 400)
        self.logText.setScaledContents(True)
        self.logText.setPixmap(QPixmap("./background/loginText.png"))  # 設定初始介面的文字標題

        self.hintText = QLabel(self)
        self.hintText.setGeometry(800, 550, 360, 260)
        self.hintText.setText("請選擇想要的桌面寵物：")
        self.hintText.setAlignment(Qt.AlignTop)  # 將對齊方式設定為 AlignTop
        self.hintText.setStyleSheet(self.style % ('#FFDEDE', '22', '標楷體', '10'))
        self.opacity_effect.setOpacity(0.8)  # 設定透明度
        self.hintText.setGraphicsEffect(self.opacity_effect)

        self.selectBox = QComboBox(self)
        self.selectBox.addItems(self.characterList)
        self.selectBox.setGeometry(805, 580, 200, 50)
        self.selectBox.setFont(QFont("標楷體", 14))

        self.sureBtn = QPushButton("Enter", self)
        self.sureBtn.setGeometry(910, 750, 100, 50)
        self.sureBtn.setStyleSheet(self.style % ('#82FFFF', '20', 'Times New Roman', '25'))
        self.sureBtn.enterEvent = self.enter_sureBtn
        self.sureBtn.mousePressEvent = self.sureBtnPressEvent

        self.exitBtn = QPushButton("Exit", self)
        self.exitBtn.setGeometry(1050, 750, 100, 50)
        self.exitBtn.setStyleSheet(self.style % ('#82FFFF', '20', 'Times New Roman', '25'))
        self.exitBtn.enterEvent = self.enter_exitBtn
        self.exitBtn.clicked.connect(self.close)
        # End.

        # ----- 設置當前版本的文字說明框 & 圖片來源 -----
        self.stateLabel = QLabel(self)
        self.stateLabel.setGeometry(350, 520, 360, 290)
        self.stateLabel.setWordWrap(True)  # 可以使 Label 顯示多行文字
        self.stateLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # 將對齊方式設定為 AlignTop

        text = "當前版本為 v1.0，目前功能/更新如下:\n" \
               "1. 新增執行程式後的視窗介面\n" \
               "2. 新增寵物: 達達利亞\n" \
               "3. 點選表情功能可以隨機更換不同圖片\n" \
               "4. 點選任意按鈕功能可以顯示不同的 icon\n" \
               "註：目前圖源皆來自網路，連結如下：\n" \

        self.stateLabel2 = QLabel(self)
        text_url = "<a href='https://www.pinterest.com'>https://www.pinterest.com</a>"
        self.stateLabel2.setText(text_url)
        self.stateLabel2.setGeometry(350, 650, 360, 30)
        self.stateLabel2.setStyleSheet(self.style % ('', '18', 'Times New Roman', '10'))
        self.stateLabel2.setOpenExternalLinks(True)  # 設定開啟外部連結

        self.stateLabel.setText(text)
        self.stateLabel.setStyleSheet(self.style % ('#B5B5B5', '18', '標楷體', '10'))
        self.opacity_effect2.setOpacity(0.8)  # 設定透明度
        self.stateLabel.setGraphicsEffect(self.opacity_effect2)
        # End.

    def enter_sureBtn(self, event):
        self.sureBtn.setCursor(QCursor(Qt.PointingHandCursor))

    def sureBtnPressEvent(self, event):
        """
        sureBtnPressEvent(self, event): 當按下 Enter 按鈕後, 進入桌面寵物視窗並隱藏原本的視窗 & 元件
        """
        self.character = self.selectBox.currentIndex()  # 讀取 QComboBox 選取的角色
        name = self.charNameList[self.character]

        self.hide()
        self.TargetPet = PetWindows(name)
        self.TargetPet.show()

    def enter_exitBtn(self, event):
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))


def WindowScreenCenter(window):
    """
    WindowScreenCenter(self, window): 將視窗設置在螢幕的中間

    Parameter:
        window: pyqt5 的視窗類別(class), 將想要設置的視窗傳到此參數

    return:
        None
    """
    screen_geometry = QDesktopWidget().availableGeometry()  # 讀取螢幕的尺寸
    windowX = (screen_geometry.width() - window.width()) // 2
    windowY = (screen_geometry.height() - window.height()) // 2
    window.move(windowX, windowY)
    pass


class PetWindows(QWidget):
    def __init__(self, name):
        super(PetWindows, self).__init__()

        # --- attribute setting ---
        # - initPetImage() 屬性 & 變數
        self.showPet = None
        self.name = name
        self.defaultImage = None
        self.PetState = None

        # - ButtonSetting() 屬性 & 變數
        self.rollButton = None
        self.emojiButton = None  # 更改成顯示自訂義表情視窗, 但要有預設值
        self.chatButton = None
        self.searchButton = None   # Wait...
        self.exitButton = None

        # - PetPressEvent() 屬性 & 變數
        self.movePet = False
        self.position = 0

        # - _emojiButtonPressEvent() 屬性 & 變數
        self.shortKeyWindow = None

        # --- 執行 class method ---
        self.initUI()
        self._classifyImg(self.name)
        self._defaultSetting(self.name)
        self.initPetImage()
        self.ButtonSetting()

    def initUI(self):
        """
        initUI(self): 初始化寵物的 UI 介面
        """
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setGeometry(0, 0, 1600, 1200)
        self.repaint()

    def _defaultSetting(self, character):
        """
        _defaultSetting(self, character): 讀取 config 資料夾裡 character 的初始設定文件

        Parameter:
            character: 載入 QComboBox 所選的寵物, 所對應的基本文件配置, str.

        Attribute:
            self.configDict: 存取寵物配置文件的資訊, dict.
        """
        # --- 讀取角色的配置文件 ---
        configPath = "./config/" + character + '.txt'
        file = open(configPath, 'r')
        configDict = dict()

        for line in file.readlines():
            line = line.rstrip().split('=')
            key, value = line
            configDict[key] = value
        # End.

        # - 設定預設資訊的屬性 -
        self.defaultCursor = QCursor(QPixmap(configDict['defaultTouchCursor']))
        self.clickCursor = QCursor(QPixmap(configDict['defaultClickCursor']))
        self.buttonStyle = configDict['buttonStyle']
        self.buttonStyle2 = configDict['buttonStyle2']
        self.touchImage = QPixmap(configDict['defaultTableImage'])
        self.moveImage = QPixmap(configDict['defaultMoveImage'])
        # End.

    def _classifyImg(self, character):
        """
        _classifyImg(self, character): 找到 character 目標寵物的資料夾下的所有圖片, 並且按照表情分類

        Parameter:
            character: 根據 QComboBox 所選的寵物, 對應的索引值名字, str.

        Attribute:
            self.emojiDict: 存放寵物不同表情的字典列表, key為該寵物的表情, value為圖片的絕對路徑. dict(list(str)).
        """
        dirName = os.getcwd() + '\\pic_' + character + "\\"
        totFiles = os.listdir(dirName)
        emojiClassify = dict()
        for file in totFiles:
            fileName = dirName + file
            key = file.split('_')[1]

            if key not in emojiClassify.keys():
                emojiClassify[key] = list()
            emojiClassify[key].append(fileName)

        self.emojiDict = emojiClassify

    def initPetImage(self):
        """
        initPetImage(self): 初始化選擇的寵物圖片, 圖片大小預設為 300x300

        Functions:
        1. 顯示寵物隨機初始的默認圖片  (OK)
        2. 當滑鼠游標接觸到圖片時, 更改滑鼠游標 icon 以及觸發顯示功能版的事件
        """
        self.showPet = QLabel(self)
        self.showPet.setGeometry(100, 100, 300, 300)
        self.showPet.setScaledContents(True)

        # --- 顯示寵物隨機初始的默認圖片, 以及初始化寵物當前狀態(心情) ---
        keys = list(self.emojiDict.keys())
        defaultEmoji = keys[np.random.randint(0, len(keys))]
        defaultImageIndex = np.random.randint(0, len(self.emojiDict[defaultEmoji]))

        pixmap = QPixmap(self.emojiDict[defaultEmoji][defaultImageIndex])
        self.showPet.setPixmap(pixmap)

        self.defaultImage = self.emojiDict[defaultEmoji][defaultImageIndex]
        self.PetState = defaultEmoji
        # End.

        # --- 當滑鼠游標接觸到圖片時, 更改滑鼠游標 icon ---
        self.showPet.setCursor(self.defaultCursor)
        self.showPet.enterEvent = self.PetEnterEvent
        self.showPet.mousePressEvent = self.PetPressEvent
        self.showPet.mouseMoveEvent = self.PetMoveEvent
        self.showPet.mouseReleaseEvent = self.PetReleaseEvent
        # End.

    def ButtonSetting(self):
        """
        ButtonSetting(self): 設定關於按鈕的功能和初始狀態

        Functions:
        1. 設定離開按鈕  (OK)
        2. 設定切換表情按鈕 (OK)
        3. 設定對話按鈕 (wait...
        4. 設定搜尋按鈕  (之後再考慮別的)
        5. 設定收起功能表按鈕  (OK)
        6. 設定按鈕滑鼠游標的 icon 事件 (OK)
        """
        # ----- Setting exitButton -----
        self.exitButton = QPushButton("離開", self)
        self.exitButton.setGeometry(350, 444, 70, 70)
        self.exitButton.setStyleSheet(self.buttonStyle)

        self.exitButton.enterEvent = self._enterButton
        self.exitButton.mousePressEvent = self._exitButtonPressEvent
        # ----- Setting exitButton -----

        # ----- Setting chatButton -----
        self.chatButton = QPushButton("對話", self)
        self.chatButton.setGeometry(400, 354, 70, 70)
        self.chatButton.setStyleSheet(self.buttonStyle2)

        self.chatButton.enterEvent = self._enterButton
        self.chatButton.mousePressEvent = self._chatButtonPressEvent
        self.chatButton.mouseReleaseEvent = self._releaseButton
        # ----- Setting chatButton -----

        # ----- Setting searchButton -----
        self.searchButton = QPushButton("搜尋", self)
        self.searchButton.setGeometry(425, 250, 70, 70)
        self.searchButton.setStyleSheet(self.buttonStyle2)

        self.searchButton.enterEvent = self._enterButton
        self.searchButton.mousePressEvent = self._searchButtonPressEvent
        self.searchButton.mouseReleaseEvent = self._releaseButton
        # ----- Setting searchButton -----

        # ----- Setting emojiButton -----
        self.emojiButton = QPushButton("表情", self)
        self.emojiButton.setGeometry(400, 144, 70, 70)
        self.emojiButton.setStyleSheet(self.buttonStyle2)

        self.emojiButton.enterEvent = self._enterButton
        self.emojiButton.mousePressEvent = self._emojiButtonPressEvent
        self.emojiButton.mouseReleaseEvent = self._releaseButton
        # ----- Setting emojiButton -----

        # ----- Setting rollButton -----
        self.rollButton = QPushButton("收起", self)
        self.rollButton.setGeometry(350, 44, 70, 70)
        self.rollButton.setStyleSheet(self.buttonStyle)
        self.rollButton.clicked.connect(self._rollback)
        # ----- Setting rollButton -----

        # Hide Button
        self.rollButton.hide()
        self.exitButton.hide()
        self.emojiButton.hide()
        self.searchButton.hide()
        self.chatButton.hide()
        pass

    def PetEnterEvent(self, event):
        """
        PetEnterEvent(self, event): 處理當滑鼠游標碰觸到圖片時的事件
        """
        self.rollButton.show()
        self.exitButton.show()
        self.emojiButton.show()
        self.searchButton.show()
        self.chatButton.show()

        self.showPet.setPixmap(self.touchImage)
        pass

    def PetPressEvent(self, event):
        """
        PetPressEvent(self, event): 處理對寵物按下滑鼠左鍵的觸發事件

        Functions:
        1. 設定滑鼠長按可以拖動寵物的 flag  (OK)
        2. Wait...
        """
        if event.button() == Qt.LeftButton:
            self.movePet = True
        self.position = event.globalPos() - self.pos()
        event.accept()
        pass

    def PetMoveEvent(self, event):
        """
        PetMoveEvent(self, event): 長按滑鼠左鍵可以使寵物移動

        Functions:
        1. 長按滑鼠左鍵可以移動寵物並在移動寵物時隱藏功能表按鈕 (OK)
        2. 切換表情/圖片 (OK)
        """
        if Qt.LeftButton and self.movePet:
            self.move(event.globalPos() - self.position)
        event.accept()

        self.rollButton.hide()
        self.exitButton.hide()
        self.emojiButton.hide()
        self.searchButton.hide()
        self.chatButton.hide()

        self.showPet.setPixmap(self.moveImage)

    def PetReleaseEvent(self, event):
        """
        PetReleaseEvent(self, event): 當滑鼠游標離開圖片時, 切換回預設圖片

        Functions:
        1. 切換回 PetEnterEvent 的圖片/表情  (OK)
        2. 將寵物可移動的 flag 設為 False  (OK)
        3. 若寵物在拖動狀態則需要切回, 點開功能表時的表情 (OK)
        """
        self.movePet = False

        if self.exitButton.isVisible():
            self.showPet.setPixmap(QPixmap(self.touchImage))

        else:
            self.showPet.setPixmap(QPixmap(self.defaultImage))
        pass

    def _enterButton(self, event):
        """
        _enterButton(self, event): 當滑鼠游標接觸到按鈕時會更改 icon

        Function:
        1. 更改游標碰觸按鈕後的 icon (OK)
        """
        self.rollButton.setCursor(self.defaultCursor)
        self.emojiButton.setCursor(self.defaultCursor)
        self.searchButton.setCursor(self.defaultCursor)
        self.chatButton.setCursor(self.defaultCursor)
        self.exitButton.setCursor(self.defaultCursor)

    def _rollback(self):
        """
        _rollback(self): 當滑鼠游標點擊"收起"按鈕後, 將隱藏功能表

        Functions:
        1. 隱藏功能表  (OK)
        2. 切換回預設表情 (OK)
        """
        self.showPet.setPixmap(QPixmap(self.defaultImage))
        self.exitButton.hide()
        self.emojiButton.hide()
        self.searchButton.hide()
        self.chatButton.hide()
        self.rollButton.hide()

    def _emojiButtonPressEvent(self, event):
        """
        _emojiButtonPressEvent(self): 當按下"表情"按鈕後, 打開快捷表情設定視窗

        Function:
        1. 更換游標圖案並且隨機切換一張圖片 (OK)
        2. 打開快捷表情視窗
        """
        # self.emojiButton.setCursor(self.clickCursor)
        # self.shortKeyWindow = ShortKeyWindow(self, self.name, self.emojiDict)
        # self.shortKeyWindow.show()

        # - 隨機切換預設圖片
        keys = list(self.emojiDict.keys())
        defaultEmoji = keys[np.random.randint(0, len(keys))]
        defaultImageIndex = np.random.randint(0, len(self.emojiDict[defaultEmoji]))
        self.defaultImage = self.emojiDict[defaultEmoji][defaultImageIndex]
        # End.

    def _chatButtonPressEvent(self, event):
        """
        _chatButtonPressEvent(self, event): wait...
        """
        self.chatButton.setCursor(self.clickCursor)
        pass

    def _searchButtonPressEvent(self, event):
        """
        _searchButtonPressEvent(self, event): wait...
        """
        self.searchButton.setCursor(self.clickCursor)
        pass

    def _exitButtonPressEvent(self, event):
        """
        _exitButtonPressEvent(self): 當按下"離開"按鈕後, 更改游標圖案並且結束程式

        Function:
        1. 更改游標圖案並且結束程式  (OK)
        """
        self.exitButton.setCursor(self.clickCursor)
        self.close()

    def _releaseButton(self, event):
        """
        _releaseButton(self, event): 設定當滑鼠游標點擊完按鈕後的狀態

        Function:
        1. 當滑鼠游標點擊按鈕後, 將游標圖片設定為預設的圖片 (OK)
        """
        self.rollButton.setCursor(self.defaultCursor)
        self.emojiButton.setCursor(self.defaultCursor)
        self.searchButton.setCursor(self.defaultCursor)
        self.chatButton.setCursor(self.defaultCursor)


class ShortKeyWindow(QWidget):
    def __init__(self, PetWindow, name, emojiDict):
        super(ShortKeyWindow, self).__init__()

        # --- attribute setting ---
        self.pet = PetWindow
        self.name = name
        self.emojiDict = emojiDict

        # - initShortKeyWindow() 屬性 & 變數
        # self.cryText = QLabel('難過', self)
        # self.fishText = QLabel('摸魚', self)
        # self.happyText = QLabel('開心', self)
        # self.seriousText = QLabel('認真', self)
        # self.shyText = QLabel('害羞', self)
        # self.thinkText = QLabel('思考', self)
        # self.tiredText = QLabel('好累', self)
        # self.emoji_lst = [
        #     (self.cryText, self.cryBox),
        #     (self.fishText, self.fishBox),
        #     (self.happyText, self.happyBox),
        #     (self.seriousText, self.seriousBox),
        #     (self.shyText, self.shyBox),
        #     (self.thinkText, self.thinkBox),
        #     (self.tiredText, self.tiredBox)
        # ]

        # --- 執行 class method ---
        self.initUI()
        self.initShortKeyWindow()

    def initUI(self):
        """
        initUI(self): 初始化的 UI 介面
        """
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(0, 0, 500, 800)
        WindowScreenCenter(self)
        self.setWindowTitle("寵物表情快捷設定")
        icon = QIcon("./pic_icon/kokomi_window_icon.png")
        self.setWindowIcon(icon)
        self.repaint()

    def initShortKeyWindow(self):
        """
        initShortKeyWindow(self): 初始化快捷表情設定視窗的樣式
        """
        # for index, item in enumerate(self.emoji_lst):
        #     item.setGeometry(10, 0 + index * 20, 100, 20)
            # QCombox 也用此種方式設定


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pet = DesktopPet()
    pet.show()
    sys.exit(app.exec_())
