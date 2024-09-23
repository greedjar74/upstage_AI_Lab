import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.express as px

def search_volume():
    path = '/Users/kimhongseok/upstage_AI_Lab/practice/EDA/tour_data_EDA/data/문화빅데이터플랫폼/월별 검색량'
    data_path_list = os.listdir(path)
    data_path_list.sort()
    data_path_list.pop(0)

    df_list = list()
    for data in data_path_list:
        df_list.append(pd.read_csv(path+'/'+data))

    search_volume_df = pd.concat([df for df in df_list]).reset_index(drop=True)
    search_volume_df['SCCNT_YM'] = pd.to_datetime(search_volume_df['SCCNT_YM'])

    key_tmp = st.text_input('관광지를 입력하세요(띄어쓰기로 구분)')
    key_list = key_tmp.split(' ')

    key_search_volume_list = list()
    for key in key_list:
        st.write('관광지:', key)
        key_search_volume = search_volume_df[search_volume_df['SRCHWRD_NM'] == key]
    
        if key_search_volume.shape[0] == 0:
            st.write('(데이터가 없습니다)')
        
        else:
            key_search_volume_list.append(key_search_volume)
            st.write(key_search_volume)
            fig = px.line(key_search_volume, x='SCCNT_YM', y='SCCNT_VALUE', markers=True)
            st.write(fig)
    if len(key_list) > 1:
        st.write('데이터 비교')
        all_key_search_volume_df = pd.concat([df for df in key_search_volume_list]).reset_index(drop=True)
        all_key_search_volume_df.sort_values('SCCNT_YM')
        st.write(all_key_search_volume_df)
        fig = px.line(all_key_search_volume_df, x='SCCNT_YM', y='SCCNT_VALUE', color='REPRSNT_KWRD_NM', markers=True, symbol='REPRSNT_KWRD_NM')
        st.write(fig)