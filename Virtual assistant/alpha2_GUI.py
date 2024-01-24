import sys
import os
import cv2

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt


class DesktopPet(QMainWindow):
    def __init__(self, ImagePath):
        super(DesktopPet, self).__init__()

        # attribute
        self.ImagePath = ImagePath
        self.showPet = None

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
        4.  重新刷新視窗和元件
        """
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setGeometry(0, 0, 1600, 1200)
        self.repaint()

    def initPetImage(self):
        """
        Method:
            initPetImage(self): 初始化寵物的圖片

        Functions:
        1. 顯示當前寵物圖片 (OK)
        2. wait...
        """
        self.showPet = QLabel(self)
        self.showPet.setGeometry(100, 100, 300, 300)
        self.showPet.setScaledContents(True)

        pixmap = QPixmap(self.ImagePath)
        self.showPet.setPixmap(pixmap)
        pass

    def ButtonSetting(self):
        """
        Method:
            ButtonSetting(self): 設定關於按鈕的功能和初始狀態
            (先不設計任何功能)

        Functions:
        1. 設定離開按鈕  (OK)
        2. 設定切換表情按鈕
        3. 設定對話按鈕
        4. 設定搜尋按鈕
        5. 設定收起功能表按鈕  (OK)
        6. Wait...
        """
        self.exitButton = QPushButton("離開", self)
        self.exitButton.setGeometry(350, 444, 70, 70)
        self.exitButton.setStyleSheet('''
                    background:#BFFFFF;
                    font:18px '微軟正黑體';
                    border-radius:35px;
                ''')
        self.exitButton.clicked.connect(self.close)

        self.chatButton = QPushButton("對話", self)
        self.chatButton.setGeometry(400, 354, 70, 70)
        self.chatButton.setStyleSheet('''
                    background:#E4BFFF;
                    font:18px '微軟正黑體';
                    border-radius:35px;
                ''')
        self.chatButton.clicked.connect(self.close)

        self.searchButton = QPushButton("搜尋", self)
        self.searchButton.setGeometry(425, 250, 70, 70)
        self.searchButton.setStyleSheet('''
                    background:#E4BFFF;
                    font:18px '微軟正黑體';
                    border-radius:35px;
                ''')
        self.searchButton.clicked.connect(self.close)

        self.emojiButton = QPushButton("表情", self)
        self.emojiButton.setGeometry(400, 144, 70, 70)
        self.emojiButton.setStyleSheet('''
                    background:#E4BFFF;
                    font:18px '微軟正黑體';
                    border-radius:35px;
                ''')
        self.emojiButton.clicked.connect(self.close)

        self.rollButton = QPushButton("收起", self)
        self.rollButton.setGeometry(350, 44, 70, 70)
        self.rollButton.setStyleSheet('''
                    background:#BFFFFF;
                    font:18px '微軟正黑體';
                    border-radius:35px;
                ''')
        self.rollButton.clicked.connect(self._rollback)

        self.rollButton.hide()
        self.exitButton.hide()
        self.emojiButton.hide()
        self.searchButton.hide()
        self.chatButton.hide()
        pass

    def enterEvent(self, event):
        """
        Method:
            enterEvent(self, event): 當滑鼠游標接觸到寵物圖像時, 會切換表情/圖片 & 滑鼠游標 & 顯示功能表

        Functions:
        1. 顯示功能表  (OK)
        2. 更改滑鼠游標 icon (OK)
        3. 切換表情/圖片
        """
        self.rollButton.show()
        self.exitButton.show()
        self.emojiButton.show()
        self.searchButton.show()
        self.chatButton.show()

        cursor = QCursor(QPixmap("./pic_icon/kokomi_fish_icon_re.png"))
        self.setCursor(cursor)
        pass

    def mousePressEvent(self, event):
        """
        Method:
            mousePressEvent(self, event): 按下滑鼠左鍵, 顯示右側功能表

        Functions:
        1.  設定滑鼠長按可以拖動寵物的 flag  (OK)
        2.  顯示右側的功能表的 flag
        """
        if event.button() == Qt.LeftButton:
            self.movePet = True
        self.position = event.globalPos() - self.pos()
        event.accept()
        pass

    def mouseMoveEvent(self, event):
        """
        Method:
            mouseMoveEvent(self, event): 長按滑鼠左鍵可以使寵物移動

        Functions:
        1. 長按滑鼠左鍵可以移動寵物 (OK)
        2. 切換表情/圖片
        """
        if Qt.LeftButton and self.movePet:
            self.move(event.globalPos() - self.position)
        event.accept()

    def mouseReleaseEvent(self, event):
        """
        Method:
            mouseReleaseEvent(self, event): 當滑鼠游標離開圖片時, 切換回預設圖片/表情

        Functions:
        1. 切換回預設圖片/表情
        2. 將寵物可移動的 flag 設為 False  (OK)
        3. wait...
        """
        self.movePet = False
        pass

    def _rollback(self):
        """
        Method:
            _rollback(self): 當滑鼠游標點擊"收起"按鈕後, 將隱藏功能表

        Functions:
        1. 隱藏功能表  (OK)
        """
        self.rollButton.hide()
        self.exitButton.hide()
        self.emojiButton.hide()
        self.searchButton.hide()
        self.chatButton.hide()
        pass


def AdjustImage(OriginalPath, TargetPath="", Xscale=0.25, Yscale=0.25):
    """利用 Opencv 調整影像大小, 並將調整後的圖片寫到 TargetPath. 預設 X, Y 皆為原來的 0.25."""
    img = cv2.imread(OriginalPath)
    y, x, _ = img.shape
    img = cv2.resize(img, (int(x * Xscale), int(y * Yscale)), cv2.LINE_AA)

    if TargetPath == "":
        filename = OriginalPath.split("\\")[-1]
        sep = filename.split(".")
        name, ext_name = sep[0], sep[1]
        newName = name + "_re." + ext_name

        TargetPath = OriginalPath.replace(filename, newName)
        cv2.imwrite(TargetPath, img)

    else:
        cv2.imwrite(TargetPath, img)

    return TargetPath


if __name__ == "__main__":
    # adjustment image size
    path = "E:\\Self-Project\\Virtual assistant\\pic_icon\\tartaglia_icon.png"
    AdjustImage(path, "", 0.1, 0.1)

    # app = QApplication(sys.argv)
    # pet = DesktopPet("E:\\Self-Project\\Virtual assistant\\pic_kokomi\\kokomi07.png")
    # pet.show()
    # sys.exit(app.exec_())

