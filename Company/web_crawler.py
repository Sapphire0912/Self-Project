import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import time
import os

url = "http://www.jnc-tec.com:11223/?key=SkVBATYwMzc5OTc4amVh&openExternalBrowser=1"

firefox_options = Options()
firefox_options.headless = True

driver = webdriver.Firefox(options=firefox_options)
driver.get(url)

time.sleep(15)
iframePage = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, "iframePage")))
driver.switch_to.frame(iframePage)

divTable = driver.find_element(By.ID, "divTable")
tbGroup43 = divTable.find_element(By.ID, "tbGroup43")
tbDevice19319 = tbGroup43.find_element(By.ID, 'tbDevice19319')
trlist = tbDevice19319.find_elements(By.CLASS_NAME, "trlist")

# 大安國中 在 index = 1, 若要取得其他 information 可以迭代 trlist
td_target = trlist[1].find_elements(By.TAG_NAME, "td")

# 點選前往查看資料 <td> search 在 index = -1
td_click = td_target[-1]
td_click.click()

time.sleep(10)
tbVDevice = driver.find_element(By.ID, "tbVDevice")
divVChannel = tbVDevice.find_element(By.ID, "divVChannel")
divTags = divVChannel.find_elements(By.TAG_NAME, "div")

# 資料在每一個 divTags 裡面的 table 底下, 並用 dict 轉成 JSON 儲存 (架設在公司的 PC 可以用 DB 來儲存)
dataDict = dict()
for info in divTags:
    eachData = info.find_elements(By.TAG_NAME, "tr")  # 有 label, value, unit 三個資訊
    label = eachData[0].text
    value = eachData[1].text
    unit = eachData[2].text
    dataDict[label] = value + unit

# 新增當前時間資訊 (先按照電腦時間為基準)
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
jsonData = dict()
jsonData[current_datetime] = dataDict

# EC > 750 要傳送到 LINE 群組警示

# 儲存成 JSON
path = "E:\\MyProgramming\\Self-Project\\Company\\datas\\Data.json"

if os.path.exists(path):
    with open(path, 'r') as file:
        saved_data = json.load(file)

    saved_data[current_datetime] = dataDict
    with open(path, 'w') as file:
        json.dump(saved_data, file, indent=4)

else:
    with open(path, 'w') as file:
        json.dump(jsonData, file, indent=4)

driver.quit()

