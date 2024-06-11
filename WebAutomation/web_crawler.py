from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from math import ceil
import random
import hashlib
import shutil
import time
import os


def calculate_file_hash(file_path, hash_type="md5"):
    """
    :param file_path: 比對的檔案名稱路徑, str
    :param hash_type: 計算 hash 的方法, 'md5' 或 'sha256'
    :return: 計算文件的 hash value
    """

    hash_function = hashlib.md5() if hash_type == "md5" else hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            # Python 3.8 寫法:
            # 相當於以下：
            # while True:
            #     chunk = f.read(8192)
            #     if not chunk:
            #         break
            hash_function.update(chunk)
    return hash_function.hexdigest()


class WebCrawler(object):
    """
    :parameter:
    :target_url: 目標連結網址
    :MAX_DOWNLOAD_COUNT: 最大嘗試下載的次數, default: 8
    """
    target_url = "https://sgw.moenv.gov.tw/SGM/Anonymous/SgmLogin.aspx"
    MAX_DOWNLOAD_COUNT = 8

    def __init__(self, update_callback, **kwargs):
        kwargs["dirPath"] = kwargs["dirPath"].replace("\\", "/")

        # -- 傳入參數 --
        self.update_callback = update_callback
        self.dirPath = kwargs["dirPath"] + "/"
        self.username = kwargs["username"]
        self.password = kwargs["pw"]
        self.downloadStatus = kwargs["status"]
        self.project_name = kwargs["project"]
        self.interval = kwargs["interval"]

        self.downloadMainDir = self.dirPath
        self.downloadTempDir = self.dirPath + "download.temp" + "/"

        if not os.path.exists(self.downloadTempDir):
            os.makedirs(self.downloadTempDir)
        # -- End. --

        # chrome 初始設定
        chrome_options = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": os.path.abspath(self.dirPath + "download.temp/"),
            "download.prompt_for_download": False,
            "directory_upgrade": True,
            "safebrowsing.enabled": True,
            "plugins.always_open_pdf_externally": True
        }

        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        # - 使用 user-agent -
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'
        ]
        chrome_options.add_argument(f"user-agent={user_agents[-1]}")
        # - End. -

        # 預設採用 Chrome 開啟 Browser
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # - 處理反爬蟲機制(清空 window.navigator) -
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            window.navigator.chrome = {
                runtime: {}
            };
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en']
            });
            """
        })
        # - End. -

        self.driver = driver
        # self.start_crawl(debug_func)

    def start_crawl(self, update_callback):
        try:
            self._login()
            time.sleep(random.uniform(2, 5))
        except Exception as e:
            update_callback(f"登入時發生錯誤：{e}")
        finally:
            self.driver.quit()

    def _login(self):
        driver = self.driver
        driver.get(self.target_url)
        self.update_callback("正在登入...")

        # 登入設定
        login_script = f"""
        arguments[0].value = {repr(self.username)};
        arguments[1].value = {repr(self.password)};
        arguments[2].click();
        """

        user = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_Txt_Acc")))
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_Txt_Pwd")))
        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_BtnLogin")))

        time.sleep(random.uniform(2, 5))
        driver.execute_script(login_script, user, password, login_btn)

        self._find_target_element()

        # 執行結束要刪掉 download.temp 的資料夾
        try:
            os.rmdir(self.dirPath + "download.temp")
        except OSError as e:
            self.update_callback(f"刪除資料夾時發生錯誤: {e}")

    def _find_target_element(self):
        driver = self.driver
        manager = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "SGM_TOP_menu_same")))
        time.sleep(random.uniform(3, 8))
        driver.execute_script('arguments[0].click();', manager)

        # 事業土地汙染調查及預防管理系統
        target_sys = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_lv_Data_ctrl8_link')))
        time.sleep(random.uniform(3, 8))
        driver.execute_script('arguments[0].click();', target_sys)
        self.update_callback("登入成功，正在進入事業土地污染調查及預防管理系統...")

        # 由於會開啟新視窗, 要偵測新視窗的位置
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        all_windows = driver.window_handles

        self.main_window = driver.current_window_handle

        for window in all_windows:
            if window != self.main_window:
                driver.switch_to.window(window)
                if driver.title == "事業土地污染調查及預防管理系統":
                    break

        # 現勘/調查/預防 -> 自主預防管理計畫資料審核 -> 環保機關檢核通過/計畫完成更新
        hover_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/OperatingFac/PhaseI/FacList.aspx']")))

        time.sleep(random.uniform(3, 8))
        actions = ActionChains(driver)
        actions.move_to_element(hover_element).perform()
        self.update_callback("導航至資料審核頁面...")

        # 等待列表的 dropdown 顯示
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".dropdown"))
        )
        target_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".dropdown li:nth-child(3) a"))
        )  # 選取列表中第三個元素
        time.sleep(random.uniform(2, 5))
        driver.execute_script('arguments[0].click();', target_link)

        # 點選相對應的選單
        project_year = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'SelPrj'))
        )
        select_project = Select(project_year)
        time.sleep(random.uniform(2, 5))
        select_project.select_by_visible_text(self.project_name)

        company_status = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'StatusId'))
        )
        select_status = Select(company_status)
        time.sleep(random.uniform(2, 5))
        select_status.select_by_visible_text(self.downloadStatus)

        # 點選查詢按鈕
        search_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'QueryBtn'))
        )
        time.sleep(0.8)
        driver.execute_script('arguments[0].click();', search_btn)

        # - 判斷已經到最後一頁的資訊 (找資料的總筆數) -
        total_data = driver.find_element(By.XPATH, "//div[@style='float: left;']")
        total = int(total_data.text.split(':')[-1])  # ...總筆數:str(count) -> total, int
        each_page_tables = driver.find_element(By.NAME, 'ctl00$ContentBody$UCPage$PageSize')
        value = int(each_page_tables.get_attribute('value'))  # 取得每頁最多顯示幾筆資料
        total_page = ceil(total / value)
        self.update_callback(f"總共找到 {total} 筆公司資料, 正在等待下載...")
        # - End. -

        # - 處理表格內的資訊 -
        for i in range(total_page):
            tab_data = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'table'))
            )
            self._extract_table_data(tab_data)

            # 回到搜尋頁面重新尋找下一頁按鈕的 element
            if i == total_page - 1:
                break

            else:
                # 瀏覽器 back() 操作 (根據每頁 table 資料數量來點 back)
                for _ in range(value):
                    time.sleep(0.5)
                    driver.back()

                # 下一頁的按鈕
                next_page_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'BtnDown'))
                )
                driver.execute_script('arguments[0].click();', next_page_btn)

        self.update_callback("資料抓取完成!")
        # - End. -
        pass

    def _extract_table_data(self, table):
        self.search_window = self.driver.current_window_handle

        # 資料在: 資料檢核表 -> 資料檢核 -> 事業自主管理計畫檢視 -> 所有的檔案名稱
        headers = [header.text for header in table.find_elements(By.XPATH, './/thead//th')]
        number_index, data_index = headers.index('管制編號'), headers.index('功能')

        # 公司名稱要用來建立資料夾名稱
        rows = table.find_elements(By.XPATH, ".//tbody//tr")
        company_dict = dict()

        for row in rows:
            td = row.find_elements(By.TAG_NAME, 'td')
            key = td[number_index].text
            a_tag = td[data_index].find_element(By.TAG_NAME, 'a')  # 資料檢核表的 id
            value = a_tag.get_attribute('href')
            company_dict[key] = value
        # {company_number: 資料檢核表 url}

        download_path = self.downloadMainDir + self.downloadStatus + "/"  # 目標上層資料夾

        for number, url in company_dict.items():
            if not os.path.isdir(download_path + number + "/"):
                os.makedirs(download_path + number + "/")
            target_path = download_path + number + "/"
            # print(f'target_path: {target_path}')
            self.update_callback(f"開始下載管制編號為 {number} 的公司資料...\n")
            time.sleep(random.uniform(2, 5))
            self._download_data(url, target_path, number)

    def _download_data(self, url, download_path, company_number):
        driver = self.driver

        driver.get(url)
        # 資料審核 ID: ui-id-2 <- a tag
        data_page = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ui-id-2')))
        time.sleep(random.uniform(2, 5))
        driver.execute_script('arguments[0].click();', data_page)

        # 事業自主審核表的按鈕在 iframe 內部
        iframe_elements = driver.find_elements(By.TAG_NAME, 'iframe')
        target_iframe = iframe_elements[1]
        time.sleep(random.uniform(3, 6))
        driver.switch_to.frame(target_iframe)

        # div class="ZoneLv1" 裡面的 a href
        div = driver.find_element(By.CLASS_NAME, 'ZoneLv1')
        a = div.find_element(By.TAG_NAME, 'a')
        time.sleep(random.uniform(2, 5))
        driver.execute_script('arguments[0].click();', a)

        # 開啟新視窗, 檔案在: 檔案名稱欄位
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))
        time.sleep(random.uniform(3, 7))
        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[-1])

        tab_data = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'table'))
        )

        headers = [header.text for header in tab_data.find_elements(By.XPATH, './/tbody//th')]
        files_index = headers.index('檔案名稱')  # index: 1
        rows = tab_data.find_elements(By.XPATH, ".//tbody//tr")

        # 要去除掉 第一行的 th
        for row in rows[1:]:
            td = row.find_elements(By.TAG_NAME, 'td')
            file_name = td[files_index].text

            # - 等待檔案下載完成 -
            try_count = 0
            while try_count <= self.MAX_DOWNLOAD_COUNT:
                try_count += 1

                # 由於下載檔案還會再多開新視窗, 要將新視窗關閉
                download_link = td[files_index].find_element(By.CSS_SELECTOR, "a[href='#']")
                time.sleep(random.uniform(4, 8))
                driver.execute_script("arguments[0].setAttribute('target', '_self');", download_link)
                download_link.click()

                self.update_callback(f"{file_name} 檔案正在下載...")
                time.sleep(self.interval[0])

                current_files = os.listdir(self.downloadTempDir)
                # - 處理在網站上下載時, 會有兩份相同檔案的問題 -
                if len(current_files) > 1:
                    # 下載至 download.temp 的 dir, 且檔案名稱更改成 company_name.file_name.extension
                    new_file_name = self.downloadTempDir + company_number + "." + file_name
                    try:
                        os.rename(os.path.join(self.downloadTempDir, current_files[0]), new_file_name)
                    except PermissionError:
                        time.sleep(self.interval[0])
                        continue
                else:
                    continue
                # - End. -

                # 將下載的檔案, 從 chrome 預設下載路徑移動到指定路徑
                if os.path.exists(new_file_name):
                    # 處理重複檔案/檔名的問題
                    try:
                        shutil.move(new_file_name, download_path)
                        time.sleep(2)
                    except shutil.Error:
                        # 利用 hash 來判斷重複檔名的檔案是否相同
                        self.update_callback(f'{new_file_name} 已在 {download_path} 裡')

                    # - 移動檔案後要刪除 download.temp 目錄下的所有檔案 -
                    for file in os.listdir(self.downloadTempDir):
                        file_name = os.path.join(self.downloadTempDir, file)
                        if os.path.isfile(file_name) or os.path.islink(file_name):
                            try:
                                os.unlink(file_name)
                            except PermissionError:
                                time.sleep(self.interval[1])
                                continue
                    # - End. -

                    time.sleep(2)

                    # 將檔案名稱修改回原本網路上的樣式
                    current_name = new_file_name.split('\\')[-1] if '\\' in new_file_name else new_file_name.split('/')[-1]
                    original_name = '.'.join(current_name.split('.')[1:])
                    try:
                        os.rename(os.path.join(download_path, current_name), os.path.join(download_path, original_name))
                    except (FileExistsError, FileNotFoundError) as e:
                        if isinstance(e, FileNotFoundError):
                            self.update_callback(f'發生 FileNotFoundError, 重新下載 {td[files_index].text} ...')
                            continue
                        elif isinstance(e, FileExistsError):
                            # 若檔名重複, 則要考慮檔案內容是否重複
                            dir_lst = os.listdir(download_path)
                            index = dir_lst.index(original_name)
                            existed_file = os.path.join(download_path, dir_lst[index])

                            # 比較 hash value
                            existed_hash = calculate_file_hash(existed_file, "md5")
                            conflict_hash = calculate_file_hash(os.path.join(download_path, current_name), "md5")
                            if existed_hash == conflict_hash:
                                os.remove(os.path.join(download_path, current_name))
                            else:
                                new_name = conflict_hash[:5] + original_name
                                os.rename(os.path.join(download_path, current_name), os.path.join(download_path, new_name))

                    break
                else:
                    self.update_callback(f'正在重新下載 {td[files_index].text} 檔案...')
                    time.sleep(random.uniform(4, 8))

            if try_count >= self.MAX_DOWNLOAD_COUNT:
                self.update_callback("超過下載次數上限，請稍後重新登入再嘗試.")

        # 檔案下載完後, 將下載的檔案引導去特定的位置; return 原本的 method 去處理
        driver.close()
        driver.switch_to.window(self.search_window)


# def debug_func(msg):
#     print(msg)
#
#
# params = {
#     "dirPath": "C:/Users/iris2/Desktop",
#     "username": 'wdlee',
#     "pw": '!Chepb1145121',
#     "status": '計畫完成更新',
#     "project": "112年度土壤及地下水污染調查及查證工作計畫-臺中市",
#     "interval": [10, 11, 12]
# }
#
# WebCrawler(debug_func, **params)
