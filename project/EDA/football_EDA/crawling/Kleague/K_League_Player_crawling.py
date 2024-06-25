from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time

url = 'https://fbref.com/en/comps/55/2023/stats/2023-K-League-1-Stats' # 2023 시즌 데이터 링크로 이동
driver = webdriver.Chrome()
driver.get(url)
#driver.implicitly_wait(5) # 웹페이지 로딩이 너무 길어서 5초 까지만 기다리고 다음 동작 실행
time.sleep(3)

#driver.find_element(By.CLASS_NAME, 'prevnext').click() # 이전 시즌으로 이동
#time.sleep(3)

# 선수 데이터가 모여있는 부분 찾기
container = driver.find_element(By.ID, 'stats_standard')
container_tmp = container.find_element(By.TAG_NAME, 'tbody') 
player_container = container_tmp.find_elements(By.TAG_NAME, 'tr') # 각각의 선수 데이터를 모두 가져와서 리스트에 저장

all_data = []

j = 0
# rank, name, nation, pos, team, age, born, mp, starts, mi, 90s, gls, ast, g+a, g-pk, pk, pkatt, yellow, red, 
for i in range(len(player_container)):
    # 중간중간 필요없는 라인은 건너뛴다.
    if i == (25 + 26*j):
        j+=1
        continue

    player = player_container[i]
    Rank = player.find_element(By.TAG_NAME, 'th').text
    td_list = player.find_elements(By.TAG_NAME, 'td')
    Name = td_list[0].text
    Nation = td_list[1].text
    Pos = td_list[2].text
    Team = td_list[3].text
    Age = td_list[4].text
    Born = td_list[5].text
    Mp = td_list[6].text
    Start = td_list[7].text
    Min = td_list[8].text
    Goals = td_list[10].text
    Ast = td_list[11].text
    G_A = td_list[12].text
    G_PK = td_list[13].text
    PK = td_list[14].text
    PKatt = td_list[15].text
    Yellow = td_list[16].text
    Red = td_list[17].text

    player_stat = [Rank, Name, Nation, Pos, Team, Age, Born, Mp, Start, Min, Goals, Ast, G_A, G_PK, PK, PKatt, Yellow, Red]
    all_data.append(player_stat)

# df형태로 변환
all_player_df = pd.DataFrame(all_data)
all_player_df.columns = ['Rank', 'Name', 'Nation', 'Pos', 'Team', 'Age', 'Born', 'Mp', 'Start', 'Min', 'Goals', 'Ast', 'G_A', 'G_PK', 'PK', 'PKatt', 'Yellow', 'Red']
print(all_player_df.head())
all_player_df.to_csv('K_league_Player_stats.csv', encoding='utf-8-sig') # 파일 생성