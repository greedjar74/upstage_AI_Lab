from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time

# 웹 페이지 생성
driver = webdriver.Chrome()
driver.get('https://1xbet.whoscored.com/')
time.sleep(2)

# 팝업 제어
#popup = driver.find_element(By.CLASS_NAME, 'webpush-swal2-container')
#popup.find_element(By.CLASS_NAME, 'webpush-swal2-close').click()
#time.sleep(1)

url_list = ['https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/9159/Stages/21087/RefereeStatistics/Italy-Serie-A-2022-2023',
            'https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/8735/Stages/19982/RefereeStatistics/Italy-Serie-A-2021-2022',
            'https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/8330/Stages/18873/RefereeStatistics/Italy-Serie-A-2020-2021',
            'https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/7928/Stages/17835/RefereeStatistics/Italy-Serie-A-2019-2020',
            'https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/7468/Stages/16548/RefereeStatistics/Italy-Serie-A-2018-2019']

year_list = ['22_23', '21_22', '20_21', '19_20', '18_19']
pages = [3, 3, 3, 2, 2]

for i in range(5):
    url = url_list[i]
    year = year_list[i]

    driver.get(url) # 해당 시즌으로 이동
    time.sleep(3)
    
    all_data = []
    for j in range(1, pages[i]+1):
        # refree 모여있는 부분 추출
        container = driver.find_element(By.ID, 'referee-tournaments-table-body')
        referee_container = container.find_elements(By.TAG_NAME, 'tr')
        if j == pages[i]:
                referee_container.pop(-1)
                
        for referee in referee_container:
            td_list = referee.find_elements(By.TAG_NAME, 'td')
            Name = td_list[0].find_element(By.CLASS_NAME, 'tournament-link').text
            Apps = int(td_list[1].text)
            Fouls_pg = float(td_list[2].text)
            Fouls_Tackles = float(td_list[3].text)
            Pen_pg = float(td_list[4].text)
            Yel_pg = float(td_list[5].text)
            Yel = int(td_list[6].text)
            Red_pg = float(td_list[7].text)
            Red = int(td_list[8].text)

            refree_data = [Name, Apps, Fouls_pg, Fouls_Tackles, Pen_pg, Yel_pg, Yel, Red_pg, Red]
            all_data.append(refree_data)
        
        if j != pages[i]:
            buttons = driver.find_element(By.ID, 'referee-stats-summary-paging')
            buttons.find_element(By.ID, 'next').click()
            time.sleep(2)

    referee_df = pd.DataFrame(all_data)
    referee_df.columns = ['Name', 'Apps', 'Fouls_pg', 'Fouls_Tackles', 'Pen_pg', 'Yel_pg', 'Yel', 'Red_pg', 'Red']
    referee_df.to_csv(f'{year}_SA_Referee_Stats.csv', encoding='utf-8-sig')
    print(referee_df.tail())