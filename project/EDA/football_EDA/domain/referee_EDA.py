import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import altair as alt

def referee_EDA():
    color_list = ['#ff7600', '#458ccc', '#d76ddb', '#8e40c0', '#8dc701']

    BL_referee = pd.read_csv('../5_seasons/referee/BL_referee_5seasons.csv')
    EPL_referee = pd.read_csv('../5_seasons/referee/EPL_referee_5seasons.csv')
    LL_referee = pd.read_csv('../5_seasons/referee/LL_referee_5seasons.csv')
    L1_referee = pd.read_csv('../5_seasons/referee/L1_referee_5seasons.csv')
    SA_referee = pd.read_csv('../5_seasons/referee/SA_referee_5seasons.csv')

    BL_referee_path_list = os.listdir('../5_seasons/Bundesliga/BL_Referee')
    EPL_referee_path_list = os.listdir('../5_seasons/EPL/EPL_Referee')
    LL_referee_path_list = os.listdir('../5_seasons/Laliga/LL_Referee')
    L1_referee_path_list = os.listdir('../5_seasons/League1/L1_Referee')
    SA_referee_path_list = os.listdir('../5_seasons/SerieA/SA_Referee')

    BL_referee_path_list.sort()
    EPL_referee_path_list.sort()
    LL_referee_path_list.sort()
    L1_referee_path_list.sort()
    SA_referee_path_list.sort()

    # 5대 리그에 대해서 5시즌 데이터를 읽어온다.
    BL_referee_data_list = []
    for path in BL_referee_path_list:
        tmp = pd.read_csv('../5_seasons/Bundesliga/BL_Referee/' + path)
        tmp.drop('Unnamed: 0', axis=1, inplace=True)
        BL_referee_data_list.append(tmp)

    EPL_referee_data_list = []
    for path in EPL_referee_path_list:
        tmp = pd.read_csv('../5_seasons/EPL/EPL_Referee/'+path)
        tmp.drop('Unnamed: 0', axis=1, inplace=True)
        EPL_referee_data_list.append(tmp)

    LL_referee_data_list = []
    for path in LL_referee_path_list:
        tmp = pd.read_csv('../5_seasons/Laliga/LL_Referee/' + path)
        tmp.drop('Unnamed: 0', axis=1, inplace=True)
        LL_referee_data_list.append(tmp)

    L1_referee_data_list = []
    for path in L1_referee_path_list:
        tmp = pd.read_csv('../5_seasons/League1/L1_Referee/' + path)
        tmp.drop('Unnamed: 0', axis=1, inplace=True)
        L1_referee_data_list.append(tmp)

    SA_referee_data_list = []
    for path in SA_referee_path_list:
        tmp = pd.read_csv('../5_seasons/SerieA/SA_Referee/' + path)
        tmp.drop('Unnamed: 0', axis=1, inplace=True)
        SA_referee_data_list.append(tmp)


    st.title('Referee EDA')

    # Yellow card 누적 그래프
    st.markdown('### 유럽 5대 리그 Yellow Card 분석')
    Yellow_tmp = []
    Yellow_tmp.append(BL_referee['Yel'].sum())
    Yellow_tmp.append(EPL_referee['Yel'].sum())
    Yellow_tmp.append(LL_referee['Yel'].sum())
    Yellow_tmp.append(L1_referee['Yel'].sum())
    Yellow_tmp.append(SA_referee['Yel'].sum())

    Yellow_df = pd.DataFrame(Yellow_tmp, index=['BL', 'EPL', 'LL', 'L1', 'SA'], columns=['Yellow'])
    #st.bar_chart(Yellow_df['Yellow']) # st.barchart를 사용해서 그래프 생성

    yel = px.bar(Yellow_df, x=['BL', 'EPL', 'LL', 'L1', 'SA'], y='Yellow', color=['BL', 'EPL', 'LL', 'L1', 'SA'], color_discrete_map={'BL': color_list[0], 'EPL': color_list[1], 'LL': color_list[2], 'L1': color_list[3], 'SA': color_list[4]})
    yel.update_xaxes(title_text="League")
    # Streamlit에 그래프 출력
    st.plotly_chart(yel)

    # 5시즌 동안 5개 리그의 Yellow카드 트렌드 그래프
    st.markdown('### 유럽 5대 리그 Yellow Card 트렌드 분석')

    BL_Yellow_trend = []
    for data in BL_referee_data_list:
        BL_Yellow_trend.append(data['Yel'].sum())

    BL_Yellow_trend_df = pd.DataFrame(BL_Yellow_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    BL_Yellow_trend_df.reset_index(inplace=True)
    BL_Yellow_trend_df.columns = ['Season', 'Yellow']

    EPL_Yellow_trend = []
    for data in EPL_referee_data_list:
        EPL_Yellow_trend.append(data['Yel'].sum())

    EPL_Yellow_trend_df = pd.DataFrame(EPL_Yellow_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    EPL_Yellow_trend_df.reset_index(inplace=True)
    EPL_Yellow_trend_df.columns = ['Season', 'Yellow']

    LL_Yellow_trend = []
    for data in LL_referee_data_list:
        LL_Yellow_trend.append(data['Yel'].sum())

    LL_Yellow_trend_df = pd.DataFrame(LL_Yellow_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    LL_Yellow_trend_df.reset_index(inplace=True)
    LL_Yellow_trend_df.columns = ['Season', 'Yellow']

    L1_Yellow_trend = []
    for data in L1_referee_data_list:
        L1_Yellow_trend.append(data['Yel'].sum())

    L1_Yellow_trend_df = pd.DataFrame(L1_Yellow_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    L1_Yellow_trend_df.reset_index(inplace=True)
    L1_Yellow_trend_df.columns = ['Season', 'Yellow']

    SA_Yellow_trend = []
    for data in SA_referee_data_list:
        SA_Yellow_trend.append(data['Yel'].sum())

    SA_Yellow_trend_df = pd.DataFrame(SA_Yellow_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    SA_Yellow_trend_df.reset_index(inplace=True)
    SA_Yellow_trend_df.columns = ['Season', 'Yellow']

    BL_Yellow_trend_df['League'] = ['BL', 'BL', 'BL', 'BL', 'BL']
    EPL_Yellow_trend_df['League'] = ['EPL', 'EPL', 'EPL', 'EPL', 'EPL']
    LL_Yellow_trend_df['League'] = ['LL', 'LL', 'LL', 'LL', 'LL']
    L1_Yellow_trend_df['League'] = ['L1', 'L1', 'L1', 'L1', 'L1']
    SA_Yellow_trend_df['League'] = ['SA', 'SA', 'SA', 'SA', 'SA']

    yel_tmp = pd.concat([BL_Yellow_trend_df, EPL_Yellow_trend_df, LL_Yellow_trend_df, L1_Yellow_trend_df, SA_Yellow_trend_df], ignore_index=True)
    yel_trend_fig = px.line(yel_tmp, x='Season', y='Yellow', color='League', markers=True, symbol='League', color_discrete_sequence=color_list)
    yel_trend_fig.update_yaxes(range=[500, 2000])
    st.write(yel_trend_fig)

    # 5대 리그 Red 카드 누적 그래프
    st.markdown('### 유럽 5대 리그 Red Card 분석')
    Red_tmp = []
    Red_tmp.append(BL_referee['Red'].sum())
    Red_tmp.append(EPL_referee['Red'].sum())
    Red_tmp.append(LL_referee['Red'].sum())
    Red_tmp.append(L1_referee['Red'].sum())
    Red_tmp.append(SA_referee['Red'].sum())

    Red_df = pd.DataFrame(Red_tmp, index=['BL', 'EPL', 'LL', 'L1', 'SA'], columns=['Red'])
    Red_df.reset_index(inplace=True)
    Red_df.columns = ['League', 'Red']

    red = px.bar(Red_df, x=['BL', 'EPL', 'LL', 'L1', 'SA'], y='Red', color=['BL', 'EPL', 'LL', 'L1', 'SA'], color_discrete_map={'BL': color_list[0], 'EPL': color_list[1], 'LL': color_list[2], 'L1': color_list[3], 'SA': color_list[4]})
    red.update_xaxes(title_text="League")
    # Streamlit에 그래프 출력
    st.plotly_chart(red)

    # 5시즌 동안 5개 리그의 Red카드 트렌드 그래프
    st.markdown('### 유럽 5대 리그 Red Card 트렌드 분석')
    
    BL_Red_trend = []
    for data in BL_referee_data_list:
        BL_Red_trend.append(data['Red'].sum())

    BL_Red_trend_df = pd.DataFrame(BL_Red_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    BL_Red_trend_df.reset_index(inplace=True)
    BL_Red_trend_df.columns = ['Season', 'Red']
    BL_Red_trend_df

    EPL_Red_trend = []
    for data in EPL_referee_data_list:
        EPL_Red_trend.append(data['Red'].sum())

    EPL_Red_trend_df = pd.DataFrame(EPL_Red_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    EPL_Red_trend_df.reset_index(inplace=True)
    EPL_Red_trend_df.columns = ['Season', 'Red']
    EPL_Red_trend_df

    LL_Red_trend = []
    for data in LL_referee_data_list:
        LL_Red_trend.append(data['Red'].sum())

    LL_Red_trend_df = pd.DataFrame(LL_Red_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    LL_Red_trend_df.reset_index(inplace=True)
    LL_Red_trend_df.columns = ['Season', 'Red']
    LL_Red_trend_df

    L1_Red_trend = []
    for data in L1_referee_data_list:
        L1_Red_trend.append(data['Red'].sum())

    L1_Red_trend_df = pd.DataFrame(L1_Red_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    L1_Red_trend_df.reset_index(inplace=True)
    L1_Red_trend_df.columns = ['Season', 'Red']
    L1_Red_trend_df

    SA_Red_trend = []
    for data in SA_referee_data_list:
        SA_Red_trend.append(data['Red'].sum())

    SA_Red_trend_df = pd.DataFrame(SA_Red_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    SA_Red_trend_df.reset_index(inplace=True)
    SA_Red_trend_df.columns = ['Season', 'Red']
    SA_Red_trend_df

    BL_Red_trend_df['League'] = ['BL', 'BL', 'BL', 'BL', 'BL']
    EPL_Red_trend_df['League'] = ['EPL', 'EPL', 'EPL', 'EPL', 'EPL']
    LL_Red_trend_df['League'] = ['LL', 'LL', 'LL', 'LL', 'LL']
    L1_Red_trend_df['League'] = ['L1', 'L1', 'L1', 'L1', 'L1']
    SA_Red_trend_df['League'] = ['SA', 'SA', 'SA', 'SA', 'SA']

    red_tmp = pd.concat([BL_Red_trend_df, EPL_Red_trend_df, LL_Red_trend_df, L1_Red_trend_df, SA_Red_trend_df], ignore_index=True)
    red_trend_fig = px.line(red_tmp, x='Season', y='Red', color='League', markers=True, symbol='League', color_discrete_sequence=color_list)
    red_trend_fig.update_yaxes(range=[0, 150])
    st.write(red_trend_fig)

    # Fouls per Tackles
    st.markdown('### 유럽 5대 리그 Fouls/Tackles 분석')
    F_per_T_tmp = []
    F_per_T_tmp.append(BL_referee['Fouls_Tackles'].sum()/BL_referee.shape[0])
    F_per_T_tmp.append(EPL_referee['Fouls_Tackles'].sum()/EPL_referee.shape[0])
    F_per_T_tmp.append(LL_referee['Fouls_Tackles'].sum()/LL_referee.shape[0])
    F_per_T_tmp.append(L1_referee['Fouls_Tackles'].sum()/L1_referee.shape[0])
    F_per_T_tmp.append(SA_referee['Fouls_Tackles'].sum()/SA_referee.shape[0])

    F_per_T_df = pd.DataFrame(F_per_T_tmp, index=['Bundesliga', 'EPL', 'Laliga', 'Ligue1', 'SerieA'], columns=['Fouls/Tackles'])
    F_per_T_df.reset_index(inplace=True)
    F_per_T_df.columns = ['League', 'Fouls/Tackles']
    

    FT = px.bar(F_per_T_df, x=['BL', 'EPL', 'LL', 'L1', 'SA'], y='Fouls/Tackles', color=['BL', 'EPL', 'LL', 'L1', 'SA'], color_discrete_map={'BL': color_list[0], 'EPL': color_list[1], 'LL': color_list[2], 'L1': color_list[3], 'SA': color_list[4]})
    FT.update_xaxes(title_text="League")
    # Streamlit에 그래프 출력
    st.plotly_chart(FT)

    # Fouls per Tackles 값 변화
    st.markdown('### 유럽 5대 리그 Fouls/Tackles 트렌드 분석')
    BL_F_per_T_trend = []
    for data in BL_referee_data_list:
        BL_F_per_T_trend.append(data['Fouls_Tackles'].sum()/data.shape[0])

    BL_F_per_T_trend_df = pd.DataFrame(BL_F_per_T_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    BL_F_per_T_trend_df.reset_index(inplace=True)
    BL_F_per_T_trend_df.columns = ['Season', 'Fouls_per_Tackles']
    BL_F_per_T_trend_df

    EPL_F_per_T_trend = []
    for data in EPL_referee_data_list:
        EPL_F_per_T_trend.append(data['Fouls_Tackles'].sum()/data.shape[0])

    EPL_F_per_T_trend_df = pd.DataFrame(EPL_F_per_T_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    EPL_F_per_T_trend_df.reset_index(inplace=True)
    EPL_F_per_T_trend_df.columns = ['Season', 'Fouls_per_Tackles']
    
    LL_F_per_T_trend = []
    for data in LL_referee_data_list:
        LL_F_per_T_trend.append(data['Fouls_Tackles'].sum()/data.shape[0])

    LL_F_per_T_trend_df = pd.DataFrame(LL_F_per_T_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    LL_F_per_T_trend_df.reset_index(inplace=True)
    LL_F_per_T_trend_df.columns = ['Season', 'Fouls_per_Tackles']

    L1_F_per_T_trend = []
    for data in L1_referee_data_list:
        L1_F_per_T_trend.append(data['Fouls_Tackles'].sum()/data.shape[0])

    L1_F_per_T_trend_df = pd.DataFrame(L1_F_per_T_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    L1_F_per_T_trend_df.reset_index(inplace=True)
    L1_F_per_T_trend_df.columns = ['Season', 'Fouls_per_Tackles']

    SA_F_per_T_trend = []
    for data in SA_referee_data_list:
        SA_F_per_T_trend.append(data['Fouls_Tackles'].sum()/data.shape[0])

    SA_F_per_T_trend_df = pd.DataFrame(SA_F_per_T_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    SA_F_per_T_trend_df.reset_index(inplace=True)
    SA_F_per_T_trend_df.columns = ['Season', 'Fouls_per_Tackles']

    BL_F_per_T_trend_df['League'] = ['BL', 'BL', 'BL', 'BL', 'BL']
    EPL_F_per_T_trend_df['League'] = ['EPL', 'EPL', 'EPL', 'EPL', 'EPL']
    LL_F_per_T_trend_df['League'] = ['LL', 'LL', 'LL', 'LL', 'LL']
    L1_F_per_T_trend_df['League'] = ['L1', 'L1', 'L1', 'L1', 'L1']
    SA_F_per_T_trend_df['League'] = ['SA', 'SA', 'SA', 'SA', 'SA']

    ft_tmp = pd.concat([BL_F_per_T_trend_df, EPL_F_per_T_trend_df, LL_F_per_T_trend_df, L1_F_per_T_trend_df, SA_F_per_T_trend_df], ignore_index=True)
    ft_trend_fig = px.line(ft_tmp, x='Season', y='Fouls_per_Tackles', color='League', markers=True, symbol='League', color_discrete_sequence=color_list)
    ft_trend_fig.update_yaxes(range=[0.5, 1])
    st.write(ft_trend_fig)

    # Fouls per Game
    st.markdown('### 유럽 5대 리그 Fouls/Game 트렌드 분석')
    BL_Fouls_pg_trend = []
    for data in BL_referee_data_list:
        BL_Fouls_pg_trend.append(data['Fouls_pg'].sum()/data.shape[0])

    BL_Fouls_pg_trend_df = pd.DataFrame(BL_Fouls_pg_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    BL_Fouls_pg_trend_df.reset_index(inplace=True)
    BL_Fouls_pg_trend_df.columns = ['Season', 'Fouls_pg']

    EPL_Fouls_pg_trend = []
    for data in EPL_referee_data_list:
        EPL_Fouls_pg_trend.append(data['Fouls_pg'].sum()/data.shape[0])

    EPL_Fouls_pg_trend_df = pd.DataFrame(EPL_Fouls_pg_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    EPL_Fouls_pg_trend_df.reset_index(inplace=True)
    EPL_Fouls_pg_trend_df.columns = ['Season', 'Fouls_pg']

    LL_Fouls_pg_trend = []
    for data in LL_referee_data_list:
        LL_Fouls_pg_trend.append(data['Fouls_pg'].sum()/data.shape[0])

    LL_Fouls_pg_trend_df = pd.DataFrame(LL_Fouls_pg_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    LL_Fouls_pg_trend_df.reset_index(inplace=True)
    LL_Fouls_pg_trend_df.columns = ['Season', 'Fouls_pg']

    L1_Fouls_pg_trend = []
    for data in L1_referee_data_list:
        L1_Fouls_pg_trend.append(data['Fouls_pg'].sum()/data.shape[0])

    L1_Fouls_pg_trend_df = pd.DataFrame(L1_Fouls_pg_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    L1_Fouls_pg_trend_df.reset_index(inplace=True)
    L1_Fouls_pg_trend_df.columns = ['Season', 'Fouls_pg']

    SA_Fouls_pg_trend = []
    for data in SA_referee_data_list:
        SA_Fouls_pg_trend.append(data['Fouls_pg'].sum()/data.shape[0])

    SA_Fouls_pg_trend_df = pd.DataFrame(SA_Fouls_pg_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
    SA_Fouls_pg_trend_df.reset_index(inplace=True)
    SA_Fouls_pg_trend_df.columns = ['Season', 'Fouls_pg']

    BL_Fouls_pg_trend_df['League'] = ['BL', 'BL', 'BL', 'BL', 'BL']
    EPL_Fouls_pg_trend_df['League'] = ['EPL', 'EPL', 'EPL', 'EPL', 'EPL']
    LL_Fouls_pg_trend_df['League'] = ['LL', 'LL', 'LL', 'LL', 'LL']
    L1_Fouls_pg_trend_df['League'] = ['L1', 'L1', 'L1', 'L1', 'L1']
    SA_Fouls_pg_trend_df['League'] = ['SA', 'SA', 'SA', 'SA', 'SA']

    fg_tmp = pd.concat([BL_Fouls_pg_trend_df, EPL_Fouls_pg_trend_df, LL_Fouls_pg_trend_df, L1_Fouls_pg_trend_df, SA_Fouls_pg_trend_df], ignore_index=True)
    fg_trend_fig = px.line(fg_tmp, x='Season', y='Fouls_pg', color='League', markers=True, symbol='League', color_discrete_sequence=color_list)
    fg_trend_fig.update_yaxes(range=[15, 30])
    st.write(fg_trend_fig)