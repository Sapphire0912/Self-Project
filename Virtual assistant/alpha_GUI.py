import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt

import cv2


class MainWindow(QMainWindow):
    def __init__(self, imagePath):
        super().__init__()

        # set windows attribute
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 加入此行會讓標題消失
        self.setAttribute(Qt.WA_TranslucentBackground)

        # set windows title & size
        self.setWindowTitle("Test")
        self.setGeometry(200, 200, 1024, 1024)  # (x, y, w, h)

        # set background image
        self.background_image = QPixmap(imagePath)
        self.background_opacity = 0.5  # setting image alpha (0 ~ 1)

        # create button
        self.button = QPushButton("按下顯示文字", self)
        self.button.setGeometry(50, 50, 200, 30)  # (x, y, w, h)
        self.button.clicked.connect(self.button_clicked)

        self.exit_button = QPushButton("結束視窗", self)
        self.exit_button.setGeometry(200, 150, 100, 40)
        self.exit_button.clicked.connect(self.close)

        # create label
        self.label = QLabel(self)
        self.label.setGeometry(50, 90, 200, 30)

        # self attribute
        self.dragPosition = None

    def button_clicked(self):
        """當按鈕被點擊後，將會執行該 method. """
        self.label.setText("Hello World!")

    def paintEvent(self, event):
        """繪製背景圖片及設定透明度"""
        painter = QPainter(self)
        painter.setOpacity(self.background_opacity)
        painter.drawPixmap(self.rect(), self.background_image)

    def mousePressEvent(self, event):
        """捕獲滑鼠左鍵按下事件，用於移動視窗"""
        if event.buttons() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        """捕獲滑鼠移動事件，用於移動視窗"""
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


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
    file = "E:\\Self-Project\\Virtual assistant\\pic\\kokomi02.jpg"
    modifyFile = AdjustImage(file)

    app = QApplication(sys.argv)

    # create main window
    window = MainWindow(modifyFile)
    window.show()
    sys.exit(app.exec_())

