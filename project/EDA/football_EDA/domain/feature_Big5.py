import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

def feature_Big5():
    FW = pd.read_csv('../5_seasons/position data/FW_5seasons.csv')
    AM = pd.read_csv('../5_seasons/position data/AM_5seasons.csv')
    M = pd.read_csv('../5_seasons/position data/M_5seasons.csv')
    DM = pd.read_csv('../5_seasons/position data/DM_5seasons.csv')
    D = pd.read_csv('../5_seasons/position data/D_5seasons.csv')
    GK = pd.read_csv('../5_seasons/position data/GK_5seasons.csv')

    FW.drop('Unnamed: 0', axis=1, inplace=True)
    AM.drop('Unnamed: 0', axis=1, inplace=True)
    M.drop('Unnamed: 0', axis=1, inplace=True)
    DM.drop('Unnamed: 0', axis=1, inplace=True)
    D.drop('Unnamed: 0', axis=1, inplace=True)
    GK.drop('Unnamed: 0', axis=1, inplace=True)

    st.header('유럽 5대 리그 포지션별 승리기여 주요 지표 추출')

    # FW
    st.write('### FW 포지션 승리기여 지표 추출')
    FW_numeric_df = FW.select_dtypes(['int64', 'float64'])
    FW_corr_matrix = FW_numeric_df.corr()
    FW_corr_matrix_Pts = FW_corr_matrix[['Pts']]
    FW_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    FW_fig = px.imshow(FW_corr_matrix_Pts)
    st.write(FW_fig)

    index_li = FW_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = FW_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # AM
    st.write('### AM 포지션 승리기여 지표 추출')
    AM_numeric_df = AM.select_dtypes(['int64', 'float64'])
    AM_corr_matrix = AM_numeric_df.corr()
    AM_corr_matrix_Pts = AM_corr_matrix[['Pts']]
    AM_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    AM_fig = px.imshow(AM_corr_matrix_Pts)
    st.write(AM_fig)

    index_li = AM_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = AM_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # M
    st.write('### M 포지션 승리기여 지표 추출')
    M_numeric_df = M.select_dtypes(['int64', 'float64'])
    M_corr_matrix = M_numeric_df.corr()
    M_corr_matrix_Pts = M_corr_matrix[['Pts']]
    M_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    M_fig = px.imshow(M_corr_matrix_Pts)
    st.write(M_fig)

    index_li = M_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = M_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # DM
    st.write('### DM 포지션 승리기여 지표 추출')
    DM_numeric_df = DM.select_dtypes(['int64', 'float64'])
    DM_corr_matrix = DM_numeric_df.corr()
    DM_corr_matrix_Pts = DM_corr_matrix[['Pts']]
    DM_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    DM_fig = px.imshow(DM_corr_matrix_Pts)
    st.write(DM_fig)

    index_li = DM_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = DM_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # D
    st.write('### D 포지션 승리기여 지표 추출')
    D_numeric_df = D.select_dtypes(['int64', 'float64'])
    D_corr_matrix = D_numeric_df.corr()
    D_corr_matrix_Pts = D_corr_matrix[['Pts']]
    D_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    D_fig = px.imshow(D_corr_matrix_Pts)
    st.write(D_fig)

    index_li = D_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = D_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # GK
    st.write('### GK 포지션 승리기여 지표 추출')
    GK_numeric_df = GK.select_dtypes(['int64', 'float64'])
    GK_corr_matrix = GK_numeric_df.corr()
    GK_corr_matrix_Pts = GK_corr_matrix[['Pts']]
    GK_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    GK_fig = px.imshow(GK_corr_matrix_Pts)
    st.write(GK_fig)

    index_li = GK_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = GK_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')