import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Firefox()

url = "https://github.com"
driver.get(url)

searchInput = driver.find_element(By.NAME,"q")

time.sleep(2)

searchInput.send_keys("python")
searchInput.send_keys(Keys.ENTER)
time.sleep(2)

driver.close()


