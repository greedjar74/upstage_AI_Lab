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

url_list = ['https://1xbet.whoscored.com/Regions/74/Tournaments/22/Seasons/9129/France-Ligue-1',
            'https://1xbet.whoscored.com/Regions/74/Tournaments/22/Seasons/8671/France-Ligue-1',
            'https://1xbet.whoscored.com/Regions/74/Tournaments/22/Seasons/8185/France-Ligue-1',
            'https://1xbet.whoscored.com/Regions/74/Tournaments/22/Seasons/7814/France-Ligue-1',
            'https://1xbet.whoscored.com/Regions/74/Tournaments/22/Seasons/7344/France-Ligue-1']

year_list = ['22_23', '21_22', '20_21', '19_20', '18_19']
id_list = ['21037', '19866', '18594', '17593', '16348']
for i in range(5):
    url = url_list[i]
    year = year_list[i]

    driver.get(url) # 해당 시즌으로 이동
    time.sleep(2)
    # team 모여있는 부분 추출
    container = driver.find_element(By.ID, f'standings-{id_list[i]}-content')
    team_container = container.find_elements(By.TAG_NAME, 'tr')
    
    all_data = []

    for team in team_container:
        tmp = team.find_element(By.CLASS_NAME, 'col12-lg-3')
        Team = tmp.find_element(By.CLASS_NAME, 'team-link').text
        P = team.find_element(By.CLASS_NAME, 'p').text # 경기수
        W = team.find_element(By.CLASS_NAME, 'w').text # 승리
        D = team.find_element(By.CLASS_NAME, 'd').text # 무승부
        L = team.find_element(By.CLASS_NAME, 'l').text # 패배
        GF = team.find_element(By.CLASS_NAME, 'gf').text # 득점
        GA = team.find_element(By.CLASS_NAME, 'ga').text # 실점
        GD = team.find_element(By.CLASS_NAME, 'gd').text # 득실차
        Pts = team.find_element(By.CLASS_NAME, 'pts').text # 승점

        team_data = [Team, P, W, D, L, GF, GA, GD, Pts]
        all_data.append(team_data)

    team_df = pd.DataFrame(all_data)
    team_df.columns = ['Team', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts']
    team_df.to_csv(f'{year}_L1_Team_Table.csv', encoding='utf-8-sig')
    print(team_df.tail())