import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

def feature_SA():
    SA_FW = pd.read_csv('../EDA/SerieA/SerieA_data/SerieA_Position_Player_Stats/SA_FW_Player.csv')
    SA_AM = pd.read_csv('../EDA/SerieA/SerieA_data/SerieA_Position_Player_Stats/SA_AM_Player.csv')
    SA_M = pd.read_csv('../EDA/SerieA/SerieA_data/SerieA_Position_Player_Stats/SA_M_Player.csv')
    SA_DM = pd.read_csv('../EDA/SerieA/SerieA_data/SerieA_Position_Player_Stats/SA_DM_Player.csv')
    SA_D = pd.read_csv('../EDA/SerieA/SerieA_data/SerieA_Position_Player_Stats/SA_D_Player.csv')
    SA_GK = pd.read_csv('../EDA/SerieA/SerieA_data/SerieA_Position_Player_Stats/SA_GK_Player.csv')

    SA_FW.drop('Unnamed: 0', axis=1, inplace=True)
    SA_AM.drop('Unnamed: 0', axis=1, inplace=True)
    SA_M.drop('Unnamed: 0', axis=1, inplace=True)
    SA_DM.drop('Unnamed: 0', axis=1, inplace=True)
    SA_D.drop('Unnamed: 0', axis=1, inplace=True)
    SA_GK.drop('Unnamed: 0', axis=1, inplace=True)

    SA_Team = pd.read_csv('../EDA/SerieA/SerieA_data/Serie_22_23_Team_Table_Added.csv')
    SA_Team.columns = ['Team', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts', 'Goals', 'Shots pg', 'Yellow', 'Red', 'Poss%', 'Pass%', 'A_Won', 'Rating', 'Shoted pg', 'Tackles pg', 'Intercept pg', 'Fouls pg', 'Offsides pg', 'Shots OT pg', 'Dribbles pg', 'Fouled pg']
    st.header('SerieA 포지션별 승리기여 주요 지표 추출')

    # FW
    st.write('### FW 포지션 승리기여 지표 추출')
    SA_FW_df = pd.merge(SA_FW,SA_Team[['Team', 'Pts']], on='Team', how='inner')
    SA_FW_numeric_df = SA_FW_df.select_dtypes(['int64', 'float64'])
    SA_FW_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    SA_FW_corr_matrix = SA_FW_numeric_df.corr()
    SA_FW_corr_matrix_Pts = SA_FW_corr_matrix[['Pts']]
    SA_FW_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    FW_fig = px.imshow(SA_FW_corr_matrix_Pts)
    st.write(FW_fig)

    index_li = SA_FW_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = SA_FW_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # AM
    st.write('### AM 포지션 승리기여 지표 추출')
    SA_AM_df = pd.merge(SA_AM, SA_Team[['Team', 'Pts']], on='Team', how='inner')
    SA_AM_numeric_df = SA_AM_df.select_dtypes(['int64', 'float64'])
    SA_AM_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    SA_AM_corr_matrix = SA_AM_numeric_df.corr()
    SA_AM_corr_matrix_Pts = SA_AM_corr_matrix[['Pts']]
    SA_AM_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    AM_fig = px.imshow(SA_AM_corr_matrix_Pts)
    st.write(AM_fig)

    index_li = SA_AM_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = SA_AM_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # M
    st.write('### M 포지션 승리기여 지표 추출')
    SA_M_df = pd.merge(SA_M, SA_Team[['Team', 'Pts']], on='Team', how='inner')
    SA_M_numeric_df = SA_M_df.select_dtypes(['int64', 'float64'])
    SA_M_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    SA_M_corr_matrix = SA_M_numeric_df.corr()
    SA_M_corr_matrix_Pts = SA_M_corr_matrix[['Pts']]
    SA_M_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    M_fig = px.imshow(SA_M_corr_matrix_Pts)
    st.write(M_fig)

    index_li = SA_M_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = SA_M_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # DM
    st.write('### DM 포지션 승리기여 지표 추출')
    SA_DM_df = pd.merge(SA_DM, SA_Team[['Team', 'Pts']], on='Team', how='inner')
    SA_DM_numeric_df = SA_DM_df.select_dtypes(['int64', 'float64'])
    SA_DM_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    SA_DM_corr_matrix = SA_DM_numeric_df.corr()
    SA_DM_corr_matrix_Pts = SA_DM_corr_matrix[['Pts']]
    SA_DM_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    DM_fig = px.imshow(SA_DM_corr_matrix_Pts)
    st.write(DM_fig)

    index_li = SA_DM_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = SA_DM_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # D
    st.write('### D 포지션 승리기여 지표 추출')
    SA_D_df = pd.merge(SA_D, SA_Team[['Team', 'Pts']], on='Team', how='inner')
    SA_D_numeric_df = SA_D_df.select_dtypes(['int64', 'float64'])
    SA_D_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    SA_D_corr_matrix = SA_D_numeric_df.corr()
    SA_D_corr_matrix_Pts = SA_D_corr_matrix[['Pts']]
    SA_D_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    D_fig = px.imshow(SA_D_corr_matrix_Pts)
    st.write(D_fig)

    index_li = SA_D_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = SA_D_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # GK
    st.write('### GK 포지션 승리기여 지표 추출')
    SA_GK_df = pd.merge(SA_GK, SA_Team[['Team', 'Pts']], on='Team', how='inner')
    SA_GK_numeric_df = SA_GK_df.select_dtypes(['int64', 'float64'])
    SA_GK_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    SA_GK_corr_matrix = SA_GK_numeric_df.corr()
    SA_GK_corr_matrix_Pts = SA_GK_corr_matrix[['Pts']]
    SA_GK_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    GK_fig = px.imshow(SA_GK_corr_matrix_Pts)
    st.write(GK_fig)

    index_li = SA_GK_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = SA_GK_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')