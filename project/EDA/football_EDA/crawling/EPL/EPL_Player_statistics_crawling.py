# 2022~2023 시즌 epl 선수 데이터 가져오기

import pandas as pd
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://1xbet.whoscored.com/Regions/252/Tournaments/2/Seasons/9075/Stages/20934/PlayerStatistics/England-Premier-League-2022-2023'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

all_data = []

for i in range(31):
    container = driver.find_element(By.ID, 'player-table-statistics-body')
    player_container = container.find_elements(By.TAG_NAME, 'tr')

    for player in player_container:
        Rank = player.find_element(By.CLASS_NAME, 'table-ranking').text
        Name = player.find_element(By.CLASS_NAME, 'iconize-icon-left').text
        Team = player.find_element(By.CLASS_NAME, 'team-name').text.replace(',', '')
        meta_datas = player.find_elements(By.CLASS_NAME, 'player-meta-data')
        tmp = meta_datas[1]
        Age = tmp.text
        tmp = meta_datas[2].text
        Position = tmp[1:]
        Apps = player.find_elements(By.TAG_NAME, 'td')[2].text
        Mins = player.find_element(By.CLASS_NAME, 'minsPlayed').text
        Goals = player.find_element(By.CLASS_NAME, 'goal').text
        Assists = player.find_element(By.CLASS_NAME, 'assistTotal').text
        Yellow = player.find_element(By.CLASS_NAME, 'yellowCard').text
        Red = player.find_element(By.CLASS_NAME, 'redCard').text
        SpG = player.find_element(By.CLASS_NAME, 'shotsPerGame').text
        PS = player.find_element(By.CLASS_NAME, 'passSuccess').text
        Aerialswon = player.find_element(By.CLASS_NAME, 'aerialWonPerGame').text
        MotM = player.find_element(By.CLASS_NAME, 'manOfTheMatch').text
        Rating = player.find_element(By.CLASS_NAME, 'rating').text

        player_data = [Rank, Name, Team, Age, Position, Apps, Mins, Goals, Assists, Yellow, Red, SpG, PS, Aerialswon, MotM, Rating]
        all_data.append(player_data)

    if i != 30:
        driver.find_element(By.ID, 'next').click()
        time.sleep(3)

all_df = pd.DataFrame(all_data)
all_df.columns = ['Rank', 'Name', 'Team', 'Age', 'Position', 'Apps', 'Mins', 'Goals', 'Assists', 'Yellow', 'Red', 'SpG', 'PS', 'Aerialswon', 'MotM', 'Rating']
all_df.to_csv('2022-2023_EPL_Player_Statistics.csv', encoding='utf-8-sig')

print(all_df.tail())