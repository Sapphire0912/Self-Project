import os
import sys
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt


def FindImage(name='kokomi'):
    """
    Function:
        FindImage(name): 找到對應名字(name)的資料夾底下的圖片

    Parameter:
        name: str, 輸入想要的角色英文名稱(皆為小寫)

    return:
        dirFiles: list(str), 回傳目標資料夾底下的檔案絕對路徑列表
    """

    # 讀取 name 的目標資料夾
    dirName = os.getcwd() + '\\pic_' + name + "\\"
    totFiles = os.listdir(dirName)
    dirFiles = list()

    for file in totFiles:
        fileName = dirName + file
        dirFiles.append(fileName)

    return dirFiles


class DesktopPet(QMainWindow):
    def __init__(self, files):
        super(DesktopPet, self).__init__()

        # attribute
        self.ImagePath = files
        self.showPet = None
        self.defaultIndex = np.random.randint(0, len(self.ImagePath))
        # self.defaultCursor = QCursor(QPixmap("./pic_icon/tartaglia_icon_re.png"))
        self.defaultCursor = QCursor(QPixmap("./pic_icon/kokomi_fish_icon_re.png"))
        self.clickCursor = QCursor(QPixmap("./pic_icon/kokomi_water_icon_re.png"))

        self.exitButton = None
        self.emojiButton = None
        self.searchButton = None
        self.chatButton = None
        self.rollButton = None

        self.movePet = False
        self.position = None

        # method
        self.initUI()
        self.initPetImage()
        self.ButtonSetting()

    def initUI(self):
        """
        Method:
            initUI(self): 初始化 UI 介面

        Functions:
        1.  隱藏視窗邊框 (OK)
        2.  視窗內部背景透明 & 視窗保持應用程式的最上層 (OK)
        3.  設定全螢幕 (1600*1200) (OK)
        4.  重新刷新視窗和元件 (OK)
        """
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setGeometry(0, 0, 1600, 1200)
        self.repaint()

    def initPetImage(self):
        """
        Method:
            initPetImage(self): 初始化寵物的圖片, 圖片大小預設 300x300

        Functions:
        1. 顯示隨機寵物圖片  (OK)
        2. 當滑鼠游標接觸到圖片時, 更改滑鼠游標 icon (OK)
        """
        self.showPet = QLabel(self)
        self.showPet.setGeometry(100, 100, 300, 300)
        self.showPet.setScaledContents(True)

        pixmap = QPixmap(self.ImagePath[self.defaultIndex])
        self.showPet.setPixmap(pixmap)

        # 關於 showPet 的 Label 所有的事件(event)
        self.showPet.setCursor(self.defaultCursor)
        self.showPet.enterEvent = self._PetEnterEvent
        self.showPet.mousePressEvent = self._PetPressEvent
        self.showPet.mouseMoveEvent = self._PetMoveEvent
        self.showPet.mouseReleaseEvent = self._PetReleaseEvent
        pass

    def ButtonSetting(self):
        """
        Method:
            ButtonSetting(self): 設定關於按鈕的功能和初始狀態
            (先不設計任何功能)

        Functions:
        1. 設定離開按鈕  (OK)
        2. 設定切換表情按鈕 (OK)
        3. 設定對話按鈕
        4. 設定搜尋按鈕
        5. 設定收起功能表按鈕  (OK)
        6. 設定按鈕滑鼠游標的 icon 事件 (OK)
        """

        # ----- Setting exitButton -----
        self.exitButton = QPushButton("離開", self)
        self.exitButton.setGeometry(350, 444, 70, 70)
        self.exitButton.setStyleSheet('''
                    background:#BFFFFF;
                    font:18px '微軟正黑體';
                    border-radius:35px;
                ''')

        self.exitButton.enterEvent = self._enterButton
        self.exitButton.mousePressEvent = self._exitButtonPressEvent
        # ----- Setting exitButton -----

        # ----- Setting chatButton -----
        self.chatButton = QPushButton("對話", self)
        self.chatButton.setGeometry(400, 354, 70, 70)
        self.chatButton.setStyleSheet('''
                    background:#E4BFFF;
                    font:18px '微軟正黑體';
                    border-radius:35px;
                ''')

        self.chatButton.enterEvent = self._enterButton
        self.chatButton.mousePressEvent = self._chatButtonPressEvent
        self.chatButton.mouseReleaseEvent = self._releaseButton
        # ----- Setting chatButton -----

        # ----- Setting searchButton -----
        self.searchButton = QPushButton("搜尋", self)
        self.searchButton.setGeometry(425, 250, 70, 70)
        self.searchButton.setStyleSheet('''
                    background:#E4BFFF;
                    font:18px '微軟正黑體';
                    border-radius:35px;
                ''')

        self.searchButton.enterEvent = self._enterButton
        self.searchButton.mousePressEvent = self._searchButtonPressEvent
        self.searchButton.mouseReleaseEvent = self._releaseButton
        # ----- Setting searchButton -----

        # ----- Setting emojiButton -----
        self.emojiButton = QPushButton("表情", self)
        self.emojiButton.setGeometry(400, 144, 70, 70)
        self.emojiButton.setStyleSheet('''
                    background:#E4BFFF;
                    font:18px '微軟正黑體';
                    border-radius:35px;
                ''')

        self.emojiButton.enterEvent = self._enterButton
        self.emojiButton.mousePressEvent = self._emojiButtonPressEvent
        self.emojiButton.mouseReleaseEvent = self._releaseButton
        # ----- Setting emojiButton -----

        # ----- Setting rollButton -----
        self.rollButton = QPushButton("收起", self)
        self.rollButton.setGeometry(350, 44, 70, 70)
        self.rollButton.setStyleSheet('''
                    background:#BFFFFF;
                    font:18px '微軟正黑體';
                    border-radius:35px;
                ''')
        self.rollButton.clicked.connect(self._rollback)
        # ----- Setting rollButton -----

        # Hide Button
        self.rollButton.hide()
        self.exitButton.hide()
        self.emojiButton.hide()
        self.searchButton.hide()
        self.chatButton.hide()
        pass

    def _PetEnterEvent(self, event):
        """
        Method:
            _PetEnterEvent(self, event): 當滑鼠游標接觸到寵物圖像時, 會切換表情/圖片 & 滑鼠游標 & 顯示功能表

        Functions:
        1. 顯示功能表  (OK)
        2. 切換表情/圖片 (OK)
        """
        self.rollButton.show()
        self.exitButton.show()
        self.emojiButton.show()
        self.searchButton.show()
        self.chatButton.show()

        # kokomi 讀書的圖片
        self.showPet.setPixmap(QPixmap("./pic_kokomi/kokomi08.png"))
        # self.showPet.setPixmap(QPixmap("./pic_tartaglia/tartaglia01.png"))
        pass

    def _PetPressEvent(self, event):
        """
        Method:
            _PetPressEvent(self, event): 按下滑鼠左鍵, 顯示右側功能表

        Functions:
        1.  設定滑鼠長按可以拖動寵物的 flag  (OK)
        2.  顯示右側的功能表的 flag
        """
        if event.button() == Qt.LeftButton:
            self.movePet = True
        self.position = event.globalPos() - self.pos()
        event.accept()
        pass

    def _PetMoveEvent(self, event):
        """
        Method:
            _PetMoveEvent(self, event): 長按滑鼠左鍵可以使寵物移動

        Functions:
        1. 長按滑鼠左鍵可以移動寵物 (OK)
        2. 切換表情/圖片 (OK)
        """
        if Qt.LeftButton and self.movePet:
            self.move(event.globalPos() - self.position)

        # kokomi 好累的圖片
        self.showPet.setPixmap(QPixmap("./pic_kokomi/kokomi06.png"))
        # self.showPet.setPixmap(QPixmap("./pic_tartaglia/tartaglia08.png"))
        event.accept()

    def _PetReleaseEvent(self, event):
        """
        Method:
            _PetReleaseEvent(self, event): 當滑鼠游標離開圖片時, 切換回和 _PetEnterEvent 一樣的圖片

        Functions:
        1. 切換回 _PetEnterEvent 的圖片/表情  (OK)
        2. 將寵物可移動的 flag 設為 False  (OK)
        3. wait...
        """
        self.movePet = False
        self.showPet.setPixmap(QPixmap("./pic_kokomi/kokomi08.png"))
        pass

    def _enterButton(self, event):
        """
        Method:
            _enterButton(self, event): 當滑鼠游標碰觸到按鈕時會更改 icon

        Functions:
        1. 更改游標碰觸按鈕後的 icon (OK)
        """
        self.rollButton.setCursor(self.defaultCursor)
        self.emojiButton.setCursor(self.defaultCursor)
        self.searchButton.setCursor(self.defaultCursor)
        self.chatButton.setCursor(self.defaultCursor)
        self.exitButton.setCursor(self.defaultCursor)

    def _rollback(self):
        """
        Method:
            _rollback(self): 當滑鼠游標點擊"收起"按鈕後, 將隱藏功能表

        Functions:
        1. 隱藏功能表  (OK)
        2. 切換回預設表情 (OK)
        """
        self.rollButton.hide()
        self.exitButton.hide()
        self.emojiButton.hide()
        self.searchButton.hide()
        self.chatButton.hide()

        self.showPet.setPixmap(QPixmap(self.ImagePath[self.defaultIndex]))
        pass

    def _emojiButtonPressEvent(self, event):
        """
        Method:
            _emojiButtonPressEvent(self): 當按下"表情"按鈕後, 更改初始預設圖片

        Function:
        1. 更改游標圖案並且結束程式  (OK)
        """
        self.emojiButton.setCursor(self.clickCursor)
        self._switchEmoji()

    def _switchEmoji(self):
        """
        Method:
            _switchEmoji(self): 當滑鼠游標點擊"收起"按鈕後, 將隨機切換預設表情

        Function:
        1. 更改與當前不同的預設表情  (OK)
        """
        current = np.random.randint(0, len(self.ImagePath))
        while current == self.defaultIndex:
            current = np.random.randint(0, len(self.ImagePath))
        self.defaultIndex = current

    def _searchButtonPressEvent(self, event):
        self.searchButton.setCursor(self.clickCursor)
        self.close()
        pass

    def _chatButtonPressEvent(self, event):
        self.chatButton.setCursor(self.clickCursor)
        self._chatEvent()
        pass

    def _chatEvent(self):
        pass

    def _exitButtonPressEvent(self, event):
        """
        Method:
            _exitButtonPressEvent(self): 當按下"離開"按鈕後, 更改游標圖案並且結束程式

        Function:
        1. 更改游標圖案並且結束程式  (OK)
        """
        self.exitButton.setCursor(self.clickCursor)
        self.close()

    def _releaseButton(self, event):
        """
        Method:
            _releaseButton(self, event): 設定當滑鼠游標點擊完按鈕後的狀態

        Function:
        1. 當滑鼠游標點擊按鈕後, 將游標圖片設定為預設的圖片 (OK)
        """
        self.rollButton.setCursor(self.defaultCursor)
        self.emojiButton.setCursor(self.defaultCursor)
        self.searchButton.setCursor(self.defaultCursor)
        self.chatButton.setCursor(self.defaultCursor)


if __name__ == "__main__":
    filesList = FindImage(name='kokomi')

    app = QApplication(sys.argv)
    pet = DesktopPet(filesList)
    pet.show()
    sys.exit(app.exec_())




