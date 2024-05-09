from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化 Selenium 的瀏覽器驅動
driver = webdriver.Firefox()
url = "http://www.jnc-tec.com:11223/?key=SkVBATYwMzc5OTc4amVh&openExternalBrowser=1"

# 打開網頁
driver.get(url)

# 等待 iframe 元素加載完畢
iframe = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))

# 切換到 iframe 元素
driver.switch_to.frame(iframe)

# 現在你可以在 iframe 內搜索元素了
table = driver.find_element(By.ID, "tbOverEndTime")
print(table)

# 找到 iframe 內的某個元素
# element = driver.find_element(By.XPATH, "//div[@class='example']")

# 輸出元素的文本內容
# print(element.text)

# 切換回主文檔
# driver.switch_to.default_content()

# 關閉瀏覽器
driver.quit()
