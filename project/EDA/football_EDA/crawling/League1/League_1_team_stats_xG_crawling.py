import pandas as pd
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://1xbet.whoscored.com/Regions/74/Tournaments/22/Seasons/9129/Stages/21037/TeamStatistics/France-Ligue-1-2022-2023'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

popup = driver.find_element(By.CLASS_NAME, 'webpush-swal2-container')
popup.find_element(By.CLASS_NAME, 'webpush-swal2-close').click()
time.sleep(1)

# xG로 이동
driver.find_element(By.XPATH, '//*[@id="stage-team-stats-options"]/li[4]/a').click()
time.sleep(3)
def_container = driver.find_element(By.ID, 'stage-team-stats-xg')
container = def_container.find_element(By.ID, 'top-team-stats-summary-content')
team_container = container.find_elements(By.TAG_NAME, 'tr')


all_data = []

for team in team_container:
    td_list = team.find_elements(By.TAG_NAME, 'td')
    tmp = td_list[0].text
    tmp_li = tmp.split('.')
    Team = tmp_li[1]
    xG = td_list[1].text
    xGDiff = td_list[3].text
    Shots = td_list[4].text
    xG_Shots = td_list[5].text

    team_data = [Team, xG, xGDiff, Shots, xG_Shots]
    all_data.append(team_data)

team_df = pd.DataFrame(all_data)    
team_df.columns = ['Team', 'xG', 'xGDiff', 'Shots', 'xG_Shots']
team_df.to_csv('2022-2023_League_1_Team_Statistics_xG.csv', encoding='utf-8-sig')
print(team_df.tail())