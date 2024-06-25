import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

def feature_EPL():
    EPL_FW = pd.read_csv('../EDA/EPL/EPL_data/EPL_Position_Player_Stats/EPL_FW_Player.csv')
    EPL_AM = pd.read_csv('../EDA/EPL/EPL_data/EPL_Position_Player_Stats/EPL_AM_Player.csv')
    EPL_M = pd.read_csv('../EDA/EPL/EPL_data/EPL_Position_Player_Stats/EPL_M_Player.csv')
    EPL_DM = pd.read_csv('../EDA/EPL/EPL_data/EPL_Position_Player_Stats/EPL_DM_Player.csv')
    EPL_D = pd.read_csv('../EDA/EPL/EPL_data/EPL_Position_Player_Stats/EPL_D_Player.csv')
    EPL_GK = pd.read_csv('../EDA/EPL/EPL_data/EPL_Position_Player_Stats/EPL_GK_Player.csv')

    EPL_FW.drop('Unnamed: 0', axis=1, inplace=True)
    EPL_AM.drop('Unnamed: 0', axis=1, inplace=True)
    EPL_M.drop('Unnamed: 0', axis=1, inplace=True)
    EPL_DM.drop('Unnamed: 0', axis=1, inplace=True)
    EPL_D.drop('Unnamed: 0', axis=1, inplace=True)
    EPL_GK.drop('Unnamed: 0', axis=1, inplace=True)

    EPL_Team = pd.read_csv('../EDA/EPL/EPL_data/EPL_Team.csv')
    EPL_Team.drop('Unnamed: 0', axis=1, inplace=True)

    st.header('EPL 포지션별 승리기여 주요 지표 추출')

    # FW
    st.write('### FW 포지션 승리기여 지표 추출')
    EPL_FW_df = pd.merge(EPL_FW, EPL_Team[['Team', 'Pts']], on='Team', how='inner')
    EPL_FW_numeric_df = EPL_FW_df.select_dtypes(['int64', 'float64'])
    EPL_FW_numeric_df.drop(['OwnG', 'Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    EPL_FW_corr_matrix = EPL_FW_numeric_df.corr()
    EPL_FW_corr_matrix_Pts = EPL_FW_corr_matrix[['Pts']]
    EPL_FW_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    FW_fig = px.imshow(EPL_FW_corr_matrix_Pts)
    st.write(FW_fig)

    index_li = EPL_FW_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = EPL_FW_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # AM
    st.write('### AM 포지션 승리기여 지표 추출')
    EPL_AM_df = pd.merge(EPL_AM, EPL_Team[['Team', 'Pts']], on='Team', how='inner')
    EPL_AM_numeric_df = EPL_AM_df.select_dtypes(['int64', 'float64'])
    EPL_AM_numeric_df.drop(['OwnG', 'Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    EPL_AM_corr_matrix = EPL_AM_numeric_df.corr()
    EPL_AM_corr_matrix_Pts = EPL_AM_corr_matrix[['Pts']]
    EPL_AM_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    AM_fig = px.imshow(EPL_AM_corr_matrix_Pts)
    st.write(AM_fig)

    index_li = EPL_AM_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = EPL_AM_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # M
    st.write('### M 포지션 승리기여 지표 추출')
    EPL_M_df = pd.merge(EPL_M, EPL_Team[['Team', 'Pts']], on='Team', how='inner')
    EPL_M_numeric_df = EPL_M_df.select_dtypes(['int64', 'float64'])
    EPL_M_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    EPL_M_corr_matrix = EPL_M_numeric_df.corr()
    EPL_M_corr_matrix_Pts = EPL_M_corr_matrix[['Pts']]
    EPL_M_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    M_fig = px.imshow(EPL_M_corr_matrix_Pts)
    st.write(M_fig)

    index_li = EPL_M_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = EPL_M_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # DM
    st.write('### DM 포지션 승리기여 지표 추출')
    EPL_DM_df = pd.merge(EPL_DM, EPL_Team[['Team', 'Pts']], on='Team', how='inner')
    EPL_DM_numeric_df = EPL_DM_df.select_dtypes(['int64', 'float64'])
    EPL_DM_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    EPL_DM_corr_matrix = EPL_DM_numeric_df.corr()
    EPL_DM_corr_matrix_Pts = EPL_DM_corr_matrix[['Pts']]
    EPL_DM_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    DM_fig = px.imshow(EPL_DM_corr_matrix_Pts)
    st.write(DM_fig)

    index_li = EPL_DM_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = EPL_DM_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # D
    st.write('### D 포지션 승리기여 지표 추출')
    EPL_D_df = pd.merge(EPL_D, EPL_Team[['Team', 'Pts']], on='Team', how='inner')
    EPL_D_numeric_df = EPL_D_df.select_dtypes(['int64', 'float64'])
    EPL_D_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    EPL_D_corr_matrix = EPL_D_numeric_df.corr()
    EPL_D_corr_matrix_Pts = EPL_D_corr_matrix[['Pts']]
    EPL_D_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    D_fig = px.imshow(EPL_D_corr_matrix_Pts)
    st.write(D_fig)

    index_li = EPL_D_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = EPL_D_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # GK
    st.write('### GK 포지션 승리기여 지표 추출')
    EPL_GK_df = pd.merge(EPL_GK, EPL_Team[['Team', 'Pts']], on='Team', how='inner')
    EPL_GK_numeric_df = EPL_GK_df.select_dtypes(['int64', 'float64'])
    EPL_GK_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
    EPL_GK_corr_matrix = EPL_GK_numeric_df.corr()
    EPL_GK_corr_matrix_Pts = EPL_GK_corr_matrix[['Pts']]
    EPL_GK_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    GK_fig = px.imshow(EPL_GK_corr_matrix_Pts)
    st.write(GK_fig)

    index_li = EPL_GK_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = EPL_GK_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')