# 2022~2023 시즌 epl 데이터 가져오기

import pandas as pd
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://1xbet.whoscored.com/Regions/252/Tournaments/2/Seasons/9075/England-Premier-League'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

container = driver.find_element(By.ID, 'standings-20934-content')
team_container = container.find_elements(By.TAG_NAME, 'tr')

all_data = []

for team in team_container:
    tmp = team.find_element(By.CLASS_NAME, 'col12-lg-3')
    Rank = tmp.find_element(By.TAG_NAME, 'span').text
    Team = tmp.find_element(By.CLASS_NAME, 'team-link').text
    P = team.find_element(By.CLASS_NAME, 'p').text
    W = team.find_element(By.CLASS_NAME, 'w').text # 승리
    D = team.find_element(By.CLASS_NAME, 'd').text # 무승부
    L = team.find_element(By.CLASS_NAME, 'l').text # 패배
    GF = team.find_element(By.CLASS_NAME, 'gf').text
    GA = team.find_element(By.CLASS_NAME, 'ga').text
    GD = team.find_element(By.CLASS_NAME, 'gd').text
    Pts = team.find_element(By.CLASS_NAME, 'pts').text

    team_data = [Rank, Team, P, W, D, L, GF, GA, GD, Pts]
    all_data.append(team_data)

team_df = pd.DataFrame(all_data)
team_df.columns = ['Rank', 'Team', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts']
team_df.to_csv('2022-2023_EPL_TEAM_Table.csv', encoding='utf-8-sig')
print(team_df.tail())