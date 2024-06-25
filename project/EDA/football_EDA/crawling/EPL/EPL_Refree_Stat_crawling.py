from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
import time

url = 'https://1xbet.whoscored.com/Regions/252/Tournaments/2/Seasons/9075/Stages/20934/RefereeStatistics/England-Premier-League-2022-2023'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

# 팝업창 있을 때 팝업 제어
popup = driver.find_element(By.CLASS_NAME, 'webpush-swal2-container')
popup.find_element(By.CLASS_NAME, 'webpush-swal2-close').click()
time.sleep(2)

container = driver.find_element(By.ID, 'referee-tournaments-table-body')
refree_container = container.find_elements(By.TAG_NAME, 'tr')

all_data = []

for refree in refree_container:
    td_list = refree.find_elements(By.TAG_NAME, 'td')
    Name = refree.find_element(By.CLASS_NAME, 'tournament-link').text
    Apps = td_list[1].text
    Fouls_pg = td_list[2].text
    Fouls_Tackles = td_list[3].text
    Pen_pg = td_list[4].text
    Yel_pg = td_list[5].text
    Yel = td_list[6].text
    Red_pg = td_list[7].text
    Red = td_list[8].text

    refree_data = [Name, Apps, Fouls_pg, Fouls_Tackles, Pen_pg, Yel_pg, Yel, Red_pg, Red]
    all_data.append(refree_data)

tmp = pd.DataFrame(all_data, columns=['Name', 'Apps', 'Fouls_pg', 'Fouls_Tackles', 'Pen_pg', 'Yel_pg', 'Yel', 'Red_pg', 'Red'])
tmp.to_csv('EPL_Refree_Stat.csv', encoding='utf-8-sig')
print(tmp.head())