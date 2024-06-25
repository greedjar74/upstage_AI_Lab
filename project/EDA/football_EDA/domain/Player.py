import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import altair as alt

def Player():
      league_features = {'1' :{'FW':['Assists', 'PS%', 'Goals'], 
                         'AM':['PS%', 'Goals', 'ThrB', 'SpG', 'Assists'],
                         'M':['PS%', 'Goals', 'AvgP', 'ThrB', 'Assists'],
                         'DM':['PS%'],
                         'D':['PS%', 'AvgP'],
                         'GK':['PS%', 'Dribble', 'Fouls', 'Disp']},
                   '2' :{'FW':['Goals', 'SpG', 'PS%', 'KeyP', 'Assists'],
                         'AM':['PS%', 'AvgP', 'Goals', 'SpG', 'Assists'],
                         'M':['Assists', 'ThrB', 'KeyP', 'LongB', 'SpG'],
                         'DM':['Assists', 'ThrB', 'Goals', 'KeyP'],
                         'D':['PS%', 'AvgP', 'ThrB', 'Assists'],
                         'GK':['PS%', 'Mins']},
                   '3' :{'FW':['PS%', 'KeyP', 'Dribble', 'ThrB', 'SpG'],
                         'AM':['AvgP', 'Assists', 'KeyP', 'ThrB', 'PS%'],
                         'M':['PS%', 'AvgP', 'Assists', 'Blocks', 'LongB'],
                         'DM':['AvgP', 'ThrB', 'PS%', 'AerialsWon', 'Fouled'],
                         'D':['PS%', 'AvgP', 'ThrB'],
                         'GK':['PS%', 'AvgP']},
                   '4':{'FW':['Assists', 'Goals'],
                        'AM':['Assists', 'PS%', 'Dribble', 'SpG', 'ThrB'],
                        'M':['PS%', 'Assists'],
                        'DM':['PS%', 'AvgP', 'LongB', 'Blocks'],
                        'D':['PS%', 'AvgP', 'Assists'],
                        'GK':['PS%', 'KeyP']},
                   '5':{'FW':['Goals', 'Assists', 'SpG', 'KeyP'],
                        'AM':['Assists'],
                        'M':['PS%'],
                        'DM':['PS%'],
                        'D':['PS%'],
                        'GK':['PS%']},
                   '6': {'FW':['Goals', 'Assists', 'SpG', 'PS%', 'ThrB'],
                         'AM':['Goals', 'Assists', 'PS%', 'SpG', 'AvgP'],
                         'M':['PS%', 'Assists', 'AvgP', 'Goals'],
                         'DM':['PS%', 'AvgP'],
                         'D':['PS%', 'AvgP'],
                         'GK':['PS%']}}

      BL_player_df = pd.read_csv('../player stats value/BL_player_stats_value.csv')
      EPL_player_df = pd.read_csv('../player stats value/EPL_player_stats_value.csv')
      LL_player_df = pd.read_csv('../player stats value/LL_player_stats_value.csv')
      L1_player_df = pd.read_csv('../player stats value/L1_player_stats_value.csv')
      SA_player_df = pd.read_csv('../player stats value/SA_player_stats_value.csv')

      BL_player_df.drop('Unnamed: 0', axis=1, inplace=True)
      EPL_player_df.drop('Unnamed: 0', axis=1, inplace=True)
      LL_player_df.drop('Unnamed: 0', axis=1, inplace=True)
      L1_player_df.drop('Unnamed: 0', axis=1, inplace=True)
      SA_player_df.drop('Unnamed: 0', axis=1, inplace=True)

      all_player_df = pd.concat([BL_player_df, EPL_player_df, LL_player_df, L1_player_df, SA_player_df], ignore_index=True)
      player_df_list = [BL_player_df, EPL_player_df, LL_player_df, L1_player_df, SA_player_df, all_player_df]

      st.header('선수 성공 여부 파악')
      player = st.text_input('선수 이름을 입력하세요')
      position = st.text_input('포지션을 입력하세요')
      league = st.text_input('리그(번호)를 선택하세요 (1.Bundesliga, 2. EPL, 3. Laliga, 4. Ligue1, 5. SerieA, 6. Big_5)')
      st.write(f'선수: {player}, 포지션: {position}, 리그: {league}')
      
      try:
            selected_player = all_player_df[all_player_df['player_name'] == player]
            features = league_features[str(league)][position]

            # 선택된 리그, 포지션에 해당하는 feature만 뽑아서 보여준다.
            selected_league_player_df = player_df_list[int(league)-1]
            selected_league_position = selected_league_player_df[selected_league_player_df['Position'] == position][features]
            selected_league_position_stats = selected_league_position.describe().loc[['mean', 'min', 'max']]
      
            for i in range(len(features)):
                  league_stats = selected_league_position_stats[[features[i]]]
                  st.write(league_stats)
                  st.write(f'Player Stats: {selected_player[features[i]].tolist()[0]}')
                  st.write('--------------------')

      except:
            st.write('해당 선수가 데이터에 없습니다. 죄송합니다.')