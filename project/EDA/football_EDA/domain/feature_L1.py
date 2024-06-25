import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

def feature_L1():
    L1_FW = pd.read_csv('../EDA/League1/League1_data/League1_Position_Player_Stats/L1_FW_Player.csv')
    L1_AM = pd.read_csv('../EDA/League1/League1_data/League1_Position_Player_Stats/L1_AM_Player.csv')
    L1_M = pd.read_csv('../EDA/League1/League1_data/League1_Position_Player_Stats/L1_M_Player.csv')
    L1_DM = pd.read_csv('../EDA/League1/League1_data/League1_Position_Player_Stats/L1_DM_Player.csv')
    L1_D = pd.read_csv('../EDA/League1/League1_data/League1_Position_Player_Stats/L1_D_Player.csv')
    L1_GK = pd.read_csv('../EDA/League1/League1_data/League1_Position_Player_Stats/L1_GK_Player.csv')

    L1_FW.drop('Unnamed: 0', axis=1, inplace=True)
    L1_AM.drop('Unnamed: 0', axis=1, inplace=True)
    L1_M.drop('Unnamed: 0', axis=1, inplace=True)
    L1_DM.drop('Unnamed: 0', axis=1, inplace=True)
    L1_D.drop('Unnamed: 0', axis=1, inplace=True)
    L1_GK.drop('Unnamed: 0', axis=1, inplace=True)

    L1_Team = pd.read_csv('../EDA/League1/League1_data/League1_22_23_Team_Table_Added.csv')
    L1_Team.drop('Unnamed: 0', axis=1, inplace=True)
    
    st.header('Ligue1 포지션별 승리기여 주요 지표 추출')

    # FW
    st.write('### FW 포지션 승리기여 지표 추출')
    L1_FW_df = pd.merge(L1_FW, L1_Team[['Team', 'Pts']], on='Team', how='inner')
    L1_FW_numeric_df = L1_FW_df.select_dtypes(['int64', 'float64'])
    L1_FW_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    L1_FW_corr_matrix = L1_FW_numeric_df.corr()
    L1_FW_corr_matrix_Pts = L1_FW_corr_matrix[['Pts']]
    L1_FW_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    FW_fig = px.imshow(L1_FW_corr_matrix_Pts)
    st.write(FW_fig)

    index_li = L1_FW_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = L1_FW_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # AM
    st.write('### AM 포지션 승리기여 지표 추출')
    L1_AM_df = pd.merge(L1_AM, L1_Team[['Team', 'Pts']], on='Team', how='inner')
    L1_AM_numeric_df = L1_AM_df.select_dtypes(['int64', 'float64'])
    L1_AM_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    L1_AM_corr_matrix = L1_AM_numeric_df.corr()
    L1_AM_corr_matrix_Pts = L1_AM_corr_matrix[['Pts']]
    L1_AM_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    AM_fig = px.imshow(L1_AM_corr_matrix_Pts)
    st.write(AM_fig)

    index_li = L1_AM_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = L1_AM_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # M
    st.write('### M 포지션 승리기여 지표 추출')
    L1_M_df = pd.merge(L1_M, L1_Team[['Team', 'Pts']], on='Team', how='inner')
    L1_M_numeric_df = L1_M_df.select_dtypes(['int64', 'float64'])
    L1_M_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    L1_M_corr_matrix = L1_M_numeric_df.corr()
    L1_M_corr_matrix_Pts = L1_M_corr_matrix[['Pts']]
    L1_M_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    M_fig = px.imshow(L1_M_corr_matrix_Pts)
    st.write(M_fig)

    index_li = L1_M_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = L1_M_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # DM
    st.write('### DM 포지션 승리기여 지표 추출')
    L1_DM_df = pd.merge(L1_DM, L1_Team[['Team', 'Pts']], on='Team', how='inner')
    L1_DM_numeric_df = L1_DM_df.select_dtypes(['int64', 'float64'])
    L1_DM_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    L1_DM_corr_matrix = L1_DM_numeric_df.corr()
    L1_DM_corr_matrix_Pts = L1_DM_corr_matrix[['Pts']]
    L1_DM_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    DM_fig = px.imshow(L1_DM_corr_matrix_Pts)
    st.write(DM_fig)

    index_li = L1_DM_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = L1_DM_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # D
    st.write('### D 포지션 승리기여 지표 추출')
    L1_D_df = pd.merge(L1_D, L1_Team[['Team', 'Pts']], on='Team', how='inner')
    L1_D_numeric_df = L1_D_df.select_dtypes(['int64', 'float64'])
    L1_D_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    L1_D_corr_matrix = L1_D_numeric_df.corr()
    L1_D_corr_matrix_Pts = L1_D_corr_matrix[['Pts']]
    L1_D_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    D_fig = px.imshow(L1_D_corr_matrix_Pts)
    st.write(D_fig)

    index_li = L1_D_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = L1_D_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # GK
    st.write('### GK 포지션 승리기여 지표 추출')
    L1_GK_df = pd.merge(L1_GK, L1_Team[['Team', 'Pts']], on='Team', how='inner')
    L1_GK_numeric_df = L1_GK_df.select_dtypes(['int64', 'float64'])
    L1_GK_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    L1_GK_corr_matrix = L1_GK_numeric_df.corr()
    L1_GK_corr_matrix_Pts = L1_GK_corr_matrix[['Pts']]
    L1_GK_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    GK_fig = px.imshow(L1_GK_corr_matrix_Pts)
    st.write(GK_fig)

    index_li = L1_GK_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = L1_GK_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')