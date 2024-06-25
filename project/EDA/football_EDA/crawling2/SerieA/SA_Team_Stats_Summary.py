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
    # team 모여있는 부분 추출
    container = driver.find_element(By.ID, 'top-team-stats-summary-content')
    team_container = container.find_elements(By.TAG_NAME, 'tr')

    all_data = []

    for team in team_container:
        tmp = team.find_element(By.CLASS_NAME, 'team-link').text
        tmp_li = tmp.split('.')
        Team = tmp_li[1][1:]
        Goals = team.find_element(By.CLASS_NAME, 'goal').text
        Shotspg = team.find_element(By.CLASS_NAME, 'shotsPerGame').text
        Yellow = team.find_element(By.CLASS_NAME, 'yellow-card-box').text
        Red = team.find_element(By.CLASS_NAME, 'red-card-box').text
        Possession = team.find_element(By.CLASS_NAME, 'possession').text
        Pass = team.find_element(By.CLASS_NAME, 'passSuccess').text
        AerialsWon = team.find_element(By.CLASS_NAME, 'aerialWonPerGame').text
        Rating = team.find_element(By.CLASS_NAME, 'sorted').text

        team_data = [Team, Goals, Shotspg, Yellow, Red, Possession, Pass, AerialsWon, Rating]
        all_data.append(team_data)

    team_df = pd.DataFrame(all_data)
    team_df.columns = ['Team', 'Goals', 'Shotspg', 'Yellow', 'Red', 'Possession', 'Pass', 'AerialsWon', 'Rating']
    team_df.to_csv(f'{year}_SA_Team_Stats_Summary.csv', encoding='utf-8-sig')
    print(team_df.tail())