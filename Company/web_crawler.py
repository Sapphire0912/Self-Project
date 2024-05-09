from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time

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

# 大安國中 在 index = 1
td_target = trlist[1].find_elements(By.TAG_NAME, "td")

# 點選前往查看資料 <td> search 在 index = -1
td_click = td_target[-1]
td_click.click()

time.sleep(10)
tbVDevice = driver.find_element(By.ID, "tbVDevice")
divVChannel = tbVDevice.find_element(By.ID, "divVChannel")
divTags = divVChannel.find_elements(By.TAG_NAME, "div")
# print(divTags[3].text)

# 資料在每一個 divTags 裡面的 table 底下
for info in divTags:
    eachData = info.find_elements(By.TAG_NAME, "tr")
    data = ''.join([i.text for i in eachData])
    print(data)

driver.quit()

