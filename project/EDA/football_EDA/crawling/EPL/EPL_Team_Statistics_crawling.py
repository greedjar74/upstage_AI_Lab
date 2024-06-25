# 2022~2023 시즌 epl 데이터 가져오기

import pandas as pd
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://1xbet.whoscored.com/Regions/252/Tournaments/2/Seasons/9075/Stages/20934/TeamStatistics/England-Premier-League-2022-2023'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

container = driver.find_element(By.ID, 'top-team-stats-summary-content')
team_container = container.find_elements(By.TAG_NAME, 'tr')

all_data = []

for team in team_container:
    tmp = team.find_element(By.CLASS_NAME, 'team-link').text
    tmp_li = tmp.split('.')
    Rank = tmp_li[0]
    Team = tmp_li[1]
    Goals = team.find_element(By.CLASS_NAME, 'goal').text
    Shotspg = team.find_element(By.CLASS_NAME, 'shotsPerGame').text
    Yellow = team.find_element(By.CLASS_NAME, 'yellow-card-box').text
    Red = team.find_element(By.CLASS_NAME, 'red-card-box').text
    Possession = team.find_element(By.CLASS_NAME, 'possession').text
    Pass = team.find_element(By.CLASS_NAME, 'passSuccess').text
    AerialsWon = team.find_element(By.CLASS_NAME, 'aerialWonPerGame').text
    Rating = team.find_element(By.CLASS_NAME, 'sorted').text

    team_data = [Rank, Team, Goals, Shotspg, Yellow, Red, Possession, Pass, AerialsWon, Rating]
    all_data.append(team_data)

team_df = pd.DataFrame(all_data)    
team_df.columns = ['Rank', 'Team', 'Goals', 'Shotspg', 'Yellow', 'Red', 'Possession', 'Pass', 'AerialsWon', 'Rating']
team_df.to_csv('2022-2023_EPL_Team_Statistics.csv', encoding='utf-8-sig')
print(team_df.tail())