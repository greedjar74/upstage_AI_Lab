import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

def feature_LL():
    LL_FW = pd.read_csv('../EDA/Laliga/Laliga_data/LL_Position_Player_Stats/LL_FW_Player.csv')
    LL_AM = pd.read_csv('../EDA/Laliga/Laliga_data/LL_Position_Player_Stats/LL_AM_Player.csv')
    LL_M = pd.read_csv('../EDA/Laliga/Laliga_data/LL_Position_Player_Stats/LL_M_Player.csv')
    LL_DM = pd.read_csv('../EDA/Laliga/Laliga_data/LL_Position_Player_Stats/LL_DM_Player.csv')
    LL_D = pd.read_csv('../EDA/Laliga/Laliga_data/LL_Position_Player_Stats/LL_D_Player.csv')
    LL_GK = pd.read_csv('../EDA/Laliga/Laliga_data/LL_Position_Player_Stats/LL_GK_Player.csv')

    LL_FW.drop('Unnamed: 0', axis=1, inplace=True)
    LL_AM.drop('Unnamed: 0', axis=1, inplace=True)
    LL_M.drop('Unnamed: 0', axis=1, inplace=True)
    LL_DM.drop('Unnamed: 0', axis=1, inplace=True)
    LL_D.drop('Unnamed: 0', axis=1, inplace=True)
    LL_GK.drop('Unnamed: 0', axis=1, inplace=True)
    

    LL_Team = pd.read_csv('../EDA/Laliga/Laliga_data/Laliga_22_23_Team_Table_Added.csv')

    st.header('Laliga 포지션별 승리기여 주요 지표 추출')

    # FW
    st.write('### FW 포지션 승리기여 지표 추출')
    LL_FW_df = pd.merge(LL_FW, LL_Team[['team_name', 'Pts']], on='team_name', how='inner')
    LL_FW_numeric_df = LL_FW_df.select_dtypes(['int64', 'float64'])
    LL_FW_numeric_df.drop(['OwnG', 'Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    LL_FW_corr_matrix = LL_FW_numeric_df.corr()
    LL_FW_corr_matrix_Pts = LL_FW_corr_matrix[['Pts']]
    LL_FW_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    FW_fig = px.imshow(LL_FW_corr_matrix_Pts)
    st.write(FW_fig)

    index_li = LL_FW_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = LL_FW_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # AM
    st.write('### AM 포지션 승리기여 지표 추출')
    LL_AM_df = pd.merge(LL_AM, LL_Team[['team_name', 'Pts']], on='team_name', how='inner')
    LL_AM_numeric_df = LL_AM_df.select_dtypes(['int64', 'float64'])
    LL_AM_numeric_df.drop(['OwnG', 'Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    LL_AM_corr_matrix = LL_AM_numeric_df.corr()
    LL_AM_corr_matrix_Pts = LL_AM_corr_matrix[['Pts']]
    LL_AM_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    AM_fig = px.imshow(LL_AM_corr_matrix_Pts)
    st.write(AM_fig)

    index_li = LL_AM_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = LL_AM_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # M
    st.write('### M 포지션 승리기여 지표 추출')
    LL_M_df = pd.merge(LL_M, LL_Team[['team_name', 'Pts']], on='team_name', how='inner')
    LL_M_numeric_df = LL_M_df.select_dtypes(['int64', 'float64'])
    LL_M_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    LL_M_corr_matrix = LL_M_numeric_df.corr()
    LL_M_corr_matrix_Pts = LL_M_corr_matrix[['Pts']]
    LL_M_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    M_fig = px.imshow(LL_M_corr_matrix_Pts)
    st.write(M_fig)

    index_li = LL_M_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = LL_M_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # DM
    st.write('### DM 포지션 승리기여 지표 추출')
    LL_DM_df = pd.merge(LL_DM, LL_Team[['team_name', 'Pts']], on='team_name', how='inner')
    LL_DM_numeric_df = LL_DM_df.select_dtypes(['int64', 'float64'])
    LL_DM_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    LL_DM_corr_matrix = LL_DM_numeric_df.corr()
    LL_DM_corr_matrix_Pts = LL_DM_corr_matrix[['Pts']]
    LL_DM_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    DM_fig = px.imshow(LL_DM_corr_matrix_Pts)
    st.write(DM_fig)

    index_li = LL_DM_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = LL_DM_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # D
    st.write('### D 포지션 승리기여 지표 추출')
    LL_D_df = pd.merge(LL_D, LL_Team[['team_name', 'Pts']], on='team_name', how='inner')
    LL_D_numeric_df = LL_D_df.select_dtypes(['int64', 'float64'])
    LL_D_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    LL_D_corr_matrix = LL_D_numeric_df.corr()
    LL_D_corr_matrix_Pts = LL_D_corr_matrix[['Pts']]
    LL_D_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    D_fig = px.imshow(LL_D_corr_matrix_Pts)
    st.write(D_fig)

    index_li = LL_D_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = LL_D_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # GK
    st.write('### GK 포지션 승리기여 지표 추출')
    LL_GK_df = pd.merge(LL_GK, LL_Team[['team_name', 'Pts']], on='team_name', how='inner')
    LL_GK_numeric_df = LL_GK_df.select_dtypes(['int64', 'float64'])
    LL_GK_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    LL_GK_corr_matrix = LL_GK_numeric_df.corr()
    LL_GK_corr_matrix_Pts = LL_GK_corr_matrix[['Pts']]
    LL_GK_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    GK_fig = px.imshow(LL_GK_corr_matrix_Pts)
    st.write(GK_fig)

    index_li = LL_GK_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = LL_GK_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')