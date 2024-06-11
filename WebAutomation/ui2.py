from PyQt5.QtWidgets import QSystemTrayIcon, QAction, QMenu
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor, QTextCursor
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5 import QtWidgets
from plyer import notification
from web_crawler import WebCrawler
import random
import sys
import os


class CrawlerWorker(QObject):
    update = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, **kwargs):
        super().__init__()
        self.crawler = WebCrawler(update_callback=self.send_update, **kwargs)
        self._is_running = True

    def send_update(self, message):
        self.update.emit(message)

    def run(self):
        try:
            self.crawler.start_crawl(self.send_update)
        except Exception as e:
            self.update.emit(f"爬蟲錯誤: {e}")
        self.finished.emit()

    def stop(self):
        self._is_running = False
        self.crawler.driver.quit()


class InitialWindow(QtWidgets.QWidget):
    __defaultPath = os.path.abspath(__file__)
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(__defaultPath))
    download_time = random.randint(10, 20)
    search_time = random.randint(10, 20)
    waiting_time = random.randint(10, 20)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("環保署網站自動化抓取檔案 v1.0")
        self.setFixedSize(600, 480)
        self.setFont(QFont('新細明體', 12))

        # 標題 icon
        titleIconPath = os.path.join(self.base_path, "images\\title_icon.ico")
        self.setWindowIcon(QIcon(titleIconPath))

        # -- 處理變數區塊 --
        # - 處理 thread 相關 -
        self.thread = None
        self.worker = None
        # - End. -

        # - 設定系統通知介面相關 -
        self.trayUI = QSystemTrayIcon(self)
        self.trayMenu = QMenu()
        # - End. -

        # - 目前專案 & 填報狀態相關 -
        self.project_label = QtWidgets.QLabel(self)
        self.project_select = QtWidgets.QComboBox(self)
        self.project_status_label = QtWidgets.QLabel(self)
        self.project_status_select = QtWidgets.QComboBox(self)
        # - End. -

        # - 選擇資料夾目錄相關 -
        self.dir_path_text = QtWidgets.QTextEdit(self)
        self.dir_choose_btn = QtWidgets.QPushButton(self)
        self.directory = os.path.dirname(self.__defaultPath)
        # - End. -

        # - 登入資訊相關 -
        self.login_description = QtWidgets.QLabel(self)
        self.acc_label = QtWidgets.QLabel(self)
        self.acc_input = QtWidgets.QLineEdit(self)
        self.pw_label = QtWidgets.QLabel(self)
        self.pw_input = QtWidgets.QLineEdit(self)
        self.login_btn = QtWidgets.QPushButton(self)
        # - End. -

        # - 錯誤訊息 & 設定相關 -
        self.config_btn = QtWidgets.QPushButton(self)
        self.error_msg_text = QtWidgets.QTextEdit(self)
        # - End. -

        # - 中止下載 & 恢復相關 -
        # self.pause_btn = QtWidgets.QPushButton(self)
        # self.continue_btn = QtWidgets.QPushButton(self)
        self.force_exit_btn = QtWidgets.QPushButton(self)
        # - End. -
        # -- End. --

        self._window_setting()
        self.ui()

    def _window_setting(self):
        # - 目前專案 & 填報狀態相關 -
        self.project_label.setGeometry(20, 20, 120, 40)
        self.project_label.setText('目前專案項目：')
        self.project_select.setGeometry(140, 25, 420, 30)

        self.project_status_label.setGeometry(52, 60, 90, 40)
        self.project_status_label.setText('填報狀態：')
        self.project_status_select.setGeometry(140, 65, 225, 30)
        # - End. -

        # - 選擇資料夾目錄相關 -
        self.dir_path_text.setGeometry(20, 110, 360, 50)
        self.dir_path_text.setReadOnly(True)
        self.dir_path_text.setText(self.directory)
        palette = self.palette()
        palette.setColor(QPalette.Base, QColor(0, 0, 0, 0))
        self.dir_path_text.setPalette(palette)
        self.dir_path_text.setStyleSheet('''border: none''')

        self.dir_choose_btn.setGeometry(390, 110, 100, 30)
        self.dir_choose_btn.setText('下載資料夾')
        self.dir_choose_btn.clicked.connect(self._dir_choose_event)
        # - End. -

        # - 登入資訊相關 -
        self.login_description.setGeometry(20, 160, 600, 20)
        self.login_description.setText("由於會不定期更新密碼, 預防帳號被鎖住, 因此先採用手動輸入登入資訊")
        self.login_description.setStyleSheet('''font-weight: bold''')

        self.acc_label.setGeometry(20, 190, 160, 30)
        self.acc_label.setText("使用者名稱 / 帳號：")
        self.acc_label.setStyleSheet('''font-weight: bold''')
        self.acc_input.setGeometry(180, 190, 150, 30)

        self.pw_label.setGeometry(120, 230, 60, 30)
        self.pw_label.setText("密碼：")
        self.pw_label.setStyleSheet('''font-weight: bold''')
        self.pw_input.setGeometry(180, 230, 150, 30)

        self.login_btn.setGeometry(350, 230, 60, 30)
        self.login_btn.setText('登入')
        # - End. -

        # - 錯誤訊息 & 設定相關 -
        self.error_msg_text.setGeometry(20, 270, 500, 140)
        self.error_msg_text.setPalette(palette)
        self.error_msg_text.setStyleSheet('''border: none''')
        self.error_msg_text.setText('訊息顯示：')
        self.error_msg_text.setReadOnly(True)

        self.config_btn.setGeometry(420, 230, 60, 30)
        self.config_btn.setText('設定')
        # - End. -

        # - 中止下載 & 恢復相關 -
        # self.pause_btn.setGeometry(20, 420, 60, 30)
        # self.pause_btn.setText('暫停')
        # self.continue_btn.setGeometry(90, 420, 60, 30)
        # self.continue_btn.setText('繼續')
        self.force_exit_btn.setGeometry(160, 420, 120, 30)
        self.force_exit_btn.setText('強制結束程式')
        # - End. -

        # - 設定系統通知介面 -
        trayIconPath = os.path.join(self.base_path, "images\\tray_icon.ico")
        self.trayUI.setIcon(QIcon(trayIconPath))
        # - End. -
        pass

    def ui(self):
        # - 目前專案 & 填報狀態相關 -
        self.project_select.addItems(["113年度土壤及地下水污染調查及查證工作計畫-臺中市", "112年度土壤及地下水污染調查及查證工作計畫-臺中市"])
        self.project_select.setCurrentIndex(1)
        self.project_status_select.addItems(["首次送出自主計畫待審核", "環保機關檢核通過", "計畫完成更新"])
        self.project_status_select.setCurrentIndex(2)
        # - End. -

        # - 登入資訊相關 -
        self.login_btn.clicked.connect(self._login_btn_event)
        # - End. -

        # - 錯誤訊息 & 設定相關 -
        self.config_btn.clicked.connect(self._config_btn_event)
        # - End. -

        # - 中止下載 & 恢復相關 -
        # self.pause_btn.clicked.connect(self._stop_btn_event)
        # self.continue_btn.clicked.connect(self._continue_btn_event)
        self.force_exit_btn.clicked.connect(self.exit_app)
        # - End. -

        # - 設定系統通知介面選單 -
        # 操作選項
        show_action = QAction("顯示視窗", self)
        hide_action = QAction("隱藏視窗", self)
        close_action = QAction("結束程式", self)

        show_action.triggered.connect(self.showNormal)
        hide_action.triggered.connect(self.hide)
        close_action.triggered.connect(self.exit_app)

        self.trayMenu.addAction(show_action)
        self.trayMenu.addAction(hide_action)
        self.trayMenu.addAction(close_action)
        self.trayUI.setContextMenu(self.trayMenu)
        self.trayUI.activated.connect(self._on_trayui_activated)
        self.trayUI.show()
        # - End. -

    def _login_btn_event(self):
        if self.acc_input.text() == '' or self.pw_input.text() == '':
            self.error_msg_text.setText('帳號或密碼不可以為空')
        else:
            self._start_crawler()

    def _start_crawler(self):
        """
        要串接的訊息:
        :parameter
        self.project_select: 當前選取的專案名稱, str
        self.project_status_select: 當前選取的填報狀態, str
        self.directory: 當前下載的資料夾目錄, str
        self.acc_input: 使用者帳號, str
        self.pw_input: 使用者密碼, str
        """
        params = {
            "dirPath": self.directory,
            "username": self.acc_input.text(),
            "pw": self.pw_input.text(),
            "status": self.project_status_select.currentText(),
            "project": self.project_select.currentText(),
            "interval": [self.download_time, self.search_time, self.waiting_time]
        }

        # 創建 QThread 和 CrawlerWorker instance
        self.thread = QThread()

        self.worker = CrawlerWorker(**params)
        self.worker.moveToThread(self.thread)
        self.worker.update.connect(self._update_thread_msg)

        self.thread.started.connect(self.worker.run)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def _update_thread_msg(self, msg):
        self.error_msg_text.append(msg)

        # 讓 cursor 移動到 TextEdit 的最底部(最新位置)
        cursor = self.error_msg_text.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.error_msg_text.setTextCursor(cursor)
        self.error_msg_text.ensureCursorVisible()

    def _config_btn_event(self):
        self.config_window = ConfigWindow(self.download_time, self.search_time, self.waiting_time)
        self.config_window.show()

    def _dir_choose_event(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, '下載目錄', os.path.dirname(self.__defaultPath))
        if directory:
            self.dir_path_text.setText(directory)
            self.directory = directory

    def _on_trayui_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.showNormal()
            self.activateWindow()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        tray_icon_path = os.path.join(self.base_path, "images\\tray_icon.ico")

        notification.notify(
            title="網頁抓取程式仍在背景執行",
            message="若要結束此程式, 請在右鍵選單中點選結束程式",
            app_icon=tray_icon_path,
            timeout=3
        )

    def exit_app(self):
        # 除了結束 UI 還要結束 Thread
        self.trayUI.hide()
        if self.thread:
            self.worker.stop()
            self.thread.quit()
        QtWidgets.QApplication.quit()


class ConfigWindow(QtWidgets.QWidget):
    def __init__(self, time1, time2, time3):
        super().__init__()

        self.setWindowTitle("爬蟲設定")
        self.setFixedSize(480, 320)
        self.setFont(QFont('新細明體', 12))
        # 標題 icon
        titleIconPath = os.path.join(InitialWindow.base_path, "images\\title_icon.ico")
        self.setWindowIcon(QIcon(titleIconPath))

        # - 調整爬蟲相關設定 -
        self.time1_label = QtWidgets.QLabel(self)
        self.time1_input = QtWidgets.QLineEdit(self)
        self.time2_label = QtWidgets.QLabel(self)
        self.time2_input = QtWidgets.QLineEdit(self)
        self.time3_label = QtWidgets.QLabel(self)
        self.time3_input = QtWidgets.QLineEdit(self)
        self.time1, self.time2, self.time3 = time1, time2, time3

        # - 確認 & 取消按鈕 -
        self.sure_btn = QtWidgets.QPushButton(self)
        self.cancel_btn = QtWidgets.QPushButton(self)
        # - End. -

        self._window_setting()
        self.ui()

    def _window_setting(self):
        # - 調整爬蟲相關設定 -
        self.time1_label.setGeometry(30, 60, 200, 40)
        self.time1_label.setText('下載檔案間隔時間(秒)：')
        self.time1_input.setGeometry(200, 68, 30, 25)
        self.time1_input.setText(str(self.time1))

        self.time2_label.setGeometry(30, 110, 200, 40)
        self.time2_label.setText('搜尋目標間隔時間(秒)：')
        self.time2_input.setGeometry(220, 118, 30, 25)
        self.time2_input.setText(str(self.time2))

        self.time3_label.setGeometry(30, 160, 200, 40)
        self.time3_label.setText('等待下載間隔時間(秒)：')
        self.time3_input.setGeometry(200, 168, 30, 25)
        self.time3_input.setText(str(self.time3))
        # - 調整爬蟲相關設定 -

        # - 確認 & 取消按鈕 -
        self.sure_btn.setGeometry(330, 260, 60, 40)
        self.sure_btn.setText('確定')
        self.cancel_btn.setGeometry(400, 260, 60, 40)
        self.cancel_btn.setText('取消')
        # - End. -
        pass

    def ui(self):
        # - 確認 & 取消按鈕 -
        self.sure_btn.clicked.connect(self._update_config)
        self.cancel_btn.clicked.connect(self.close)
        # - End. -

    def _update_config(self):
        time1, time2, time3 = self.time1_input.text(), self.time2_input.text(), self.time3_input.text()
        InitialWindow.time1 = float(time1)
        InitialWindow.time2 = float(time2)
        InitialWindow.time3 = float(time3)
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # 避免應用程式退出
    window = InitialWindow()
    window.show()
    sys.exit(app.exec_())
