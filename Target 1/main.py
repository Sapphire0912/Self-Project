from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import requests
import numpy as np
import cv2
import time

# 利用 selenium webdriver 中的 firefox service 創建一個 firefox Service(Path: 為 geckodriver 的執行檔路徑)
# 註: 若要使用 selenium 來請求進入網頁, 瀏覽器需要一個 driver(ex. firefox 為 geckodriver)
# WebService = webdriver.firefox.service.Service(r"C:\\Program Files\\Mozilla Firefox\\geckodriver.exe")
# WebDriver = webdriver.Firefox(service=WebService)
# WebDriver.get("https://yande.re/")  # 連接到目的地的網頁
# WebDriver.close()


class Yande(object):
    def __init__(self):
        self.YandeURL = "https://yande.re/"

        self.ThumbnailLink = list()
        self.OriginalLink = list()
        self.ImageTags = None

        self.URLMaxPage = 1
        self.FileName = ''
        self.CurrPage = 1

        # 網頁分析
        self._WebAnalyze(self.YandeURL)

    def _WebAnalyze(self, url):
        print(f'Current URL: {url}')

        response = requests.get(url)
        if response.status_code == 404:
            raise RuntimeError(f"{self.YandeURL} Not Found")

        soup = BeautifulSoup(response.text, "html.parser")

        pagination = soup.find(class_="pagination")
        MaxPage = int(pagination.find_all('a')[-2]["aria-label"].split(' ')[-1])

        imgTag = soup.find_all(class_='thumb')

        self.ImageTags = imgTag
        self.URLMaxPage = MaxPage

    def DownLoad(self, page, OutputDir, Tag=None, LargeVersion=False):
        """
        到 Yande.re 網頁下載圖片的主程式

        parameters:
        page: 指定要下載的頁數或範圍; all 代表全部, 否則輸入頁數 list(int)
        """
        self.FileName = Tag

        if isinstance(page, str):
            if page.lower() == 'all':
                max_page = self.URLMaxPage

                for _page in range(max_page):
                    if Tag is None:
                        URL_format = f'post?page={_page}'
                    else:
                        URL_format = f'post?page={_page}&tags={Tag}'

                    SearchTagURL = self.YandeURL + URL_format

                    self.CurrPage = _page
                    self._WebAnalyze(SearchTagURL)
                    self._DownLoadTarget(OutputDir, LargeVersion)

            else:
                raise ValueError(f"page 的格式錯誤, 'all' 或 list of integers")

        elif isinstance(page, list):
            for _page in page:
                if Tag is None:
                    URL_format = f'post?page={_page}'
                else:
                    URL_format = f'post?page={_page}&tags={Tag}'

                SearchTagURL = self.YandeURL + URL_format

                self.CurrPage = _page
                self._WebAnalyze(SearchTagURL)
                self._DownLoadTarget(OutputDir, LargeVersion)

        else:
            raise ValueError(f"page 的格式錯誤, 'all' 或 list of integers")

    def _DownLoadTarget(self, OutputDir, LargeVersion=False):
        imgTag = self.ImageTags
        curr_page = self.CurrPage

        for index, tag in enumerate(imgTag):
            img_info = tag.find('img')

            if self.FileName != '':
                FileName = self.FileName + str(index + (curr_page - 1) * 40 + 1)
            else:
                FileName = tag["href"][1:].replace('/', '_')

            # print(img_info["alt"], type(img_info["alt"]))  # other information, 未來可以設計分類器用的其中一項
            self.ThumbnailLink.append(img_info["src"])  # 縮圖的 url
            AccessImgPage = tag.get_text().split(' ')[-1]  # 原圖的 url

            print(f'Access Image Link: {AccessImgPage}')

            response2 = requests.get(AccessImgPage)

            if response2.status_code == 404:
                raise RuntimeError(f"{AccessImgPage} Not Found")

            soup2 = BeautifulSoup(response2.text, "html.parser")

            if LargeVersion:
                TargetURL = soup2.find(class_="original-file-changed highres-show")["href"]
            else:
                TargetURL = soup2.find_all("img")[-1]["src"]

            largeVersion = requests.get(TargetURL).content
            ImgArray = np.frombuffer(largeVersion, np.uint8)
            Img = cv2.imdecode(ImgArray, cv2.IMREAD_COLOR)

            writePath = OutputDir + FileName + '.png'
            print(f'Save Path: {writePath}\n')

            cv2.imwrite(writePath, Img)


alpha = Yande()
alpha.DownLoad(
    page=[1, 2],
    Tag='hakui_koyori',
    OutputDir="E:\\Self-Project\\Target 1\\Download pic\\",
    LargeVersion=False
)



