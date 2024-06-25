from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://data.kma.go.kr/data/ogd/selectGtsRltmList.do?pgmNo=658'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

driver.find_element(By.ID, 'ztree_34_switch').click()
time.sleep(0.5)
driver.find_element(By.ID, 'ztree_46_check').click()
time.sleep(1)

driver.find_element(By.ID, 'startDt_d').click()
time.sleep(0.3)