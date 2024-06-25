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

url_list = ['https://1xbet.whoscored.com/Regions/252/Tournaments/2/Seasons/9075/Stages/20934/PlayerStatistics/England-Premier-League-2022-2023',
            'https://1xbet.whoscored.com/Regions/252/Tournaments/2/Seasons/8618/Stages/19793/PlayerStatistics/England-Premier-League-2021-2022',
            'https://1xbet.whoscored.com/Regions/252/Tournaments/2/Seasons/8228/Stages/18685/PlayerStatistics/England-Premier-League-2020-2021',
            'https://1xbet.whoscored.com/Regions/252/Tournaments/2/Seasons/7811/Stages/17590/PlayerStatistics/England-Premier-League-2019-2020',
            'https://1xbet.whoscored.com/Regions/252/Tournaments/2/Seasons/7361/Stages/16368/PlayerStatistics/England-Premier-League-2018-2019']

year_list = ['22_23', '21_22', '20_21', '19_20', '18_19']
next_tap = [31, 30, 30, 28, 29]

for i in range(5):
    url = url_list[i]
    year = year_list[i]

    driver.get(url) # 해당 시즌으로 이동
    time.sleep(3)
    # defnsive로 이동
    driver.find_element(By.XPATH, '//*[@id="stage-top-player-stats-options"]/li[4]/a').click()
    time.sleep(3)

    all_data = []
    for j in range(next_tap[i]):
        container_tmp = driver.find_element(By.ID, 'statistics-table-defensive')
        container = container_tmp.find_element(By.ID, 'player-table-statistics-body')
        player_container = container.find_elements(By.TAG_NAME, 'tr')

        for player in player_container:
            Name = player.find_element(By.CLASS_NAME, 'iconize-icon-left').text
            AvgP = player.find_element(By.CLASS_NAME, 'totalPassesPerGame').text
            PSp = player.find_element(By.CLASS_NAME, 'passSuccess').text
            Crosses = player.find_element(By.CLASS_NAME, 'accurateCrossesPerGame').text
            LonB = player.find_element(By.CLASS_NAME, 'accurateLongPassPerGame').text
            ThrB = player.find_element(By.CLASS_NAME, 'accurateThroughBallPerGame').text

            player_data = [Name, AvgP, PSp, Crosses, LonB, ThrB]
            all_data.append(player_data)
        
        if j != next_tap[i]:
            buttons = driver.find_element(By.ID, 'statistics-paging-offensive')
            buttons.find_element(By.ID, 'next').click()
            time.sleep(2)

    player_df = pd.DataFrame(all_data)    
    player_df.columns = ['Name', 'AvgP', 'PSp', 'Crosses', 'LonB', 'ThrB']
    player_df.to_csv(f'{year}_EPL_Player_Stats_Pass.csv', encoding='utf-8-sig')
    print(player_df.tail())