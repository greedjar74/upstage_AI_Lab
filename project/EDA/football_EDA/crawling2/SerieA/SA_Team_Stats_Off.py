from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time

# 웹 페이지 생성
driver = webdriver.Chrome()
driver.get('https://1xbet.whoscored.com/')
time.sleep(1)

# 팝업 제어
#popup = driver.find_element(By.CLASS_NAME, 'webpush-swal2-container')
#popup.find_element(By.CLASS_NAME, 'webpush-swal2-close').click()
#time.sleep(1)

url_list = ['https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/9159/Stages/21087/TeamStatistics/Italy-Serie-A-2022-2023',
            'https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/8735/Stages/19982/TeamStatistics/Italy-Serie-A-2021-2022',
            'https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/8330/Stages/18873/TeamStatistics/Italy-Serie-A-2020-2021',
            'https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/7928/Stages/17835/TeamStatistics/Italy-Serie-A-2019-2020',
            'https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/7468/Stages/16548/TeamStatistics/Italy-Serie-A-2018-2019']

year_list = ['22_23', '21_22', '20_21', '19_20', '18_19']
for i in range(5):
    url = url_list[i]
    year = year_list[i]

    driver.get(url) # 해당 시즌으로 이동
    time.sleep(3)

    # Offensive로 이동
    driver.find_element(By.XPATH, '//*[@id="stage-team-stats-options"]/li[3]/a').click()
    time.sleep(2)
    off_container = driver.find_element(By.ID, 'stage-team-stats-offensive')
    container = off_container.find_element(By.ID, 'top-team-stats-summary-content')
    team_container = container.find_elements(By.TAG_NAME, 'tr')

    all_data = []

    for team in team_container:
        td_list = team.find_elements(By.TAG_NAME, 'td')
        tmp = td_list[0].text
        tmp_li = tmp.split('.')
        Team = tmp_li[1][1:]
        Shotspg = td_list[1].text
        ShotsOTpg = td_list[2].text
        Dribblespg = td_list[3].text
        Fouledpg = td_list[4].text

        team_data = [Team, Shotspg, ShotsOTpg, Dribblespg, Fouledpg]
        all_data.append(team_data)

    team_df = pd.DataFrame(all_data)    
    team_df.columns = ['Team', 'of_Shotspg', 'of_ShotsOTpg', 'of_Dribblespg', 'of_Fouledpg']
    team_df.to_csv(f'{year}_SA_Team_Stats_offensive.csv', encoding='utf-8-sig')
    print(team_df.tail())