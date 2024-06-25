import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
from PIL import Image

from referee_main import referee_main
from feature_main import feature_main
from Player import Player

# 페이지 선언 
def main_page():
    st.title('Football EDA')
    st.write('### 내가 분석한 내용 구경해볼래?')
    st.sidebar.write('### 리그별 승리 주요 지표')
    st.sidebar.write('### Referee EDA')
    st.sidebar.write('### 선수 성공여부 파악')
    main_image = Image.open('../image/main.jpg')
    st.write(main_image)
    st.write('???: 궁금해서 뛰어가는 중')

def page2():
    feature_main()
    st.sidebar.title('승리 기여 주요 지표')

def page3():
    referee_main()
    st.sidebar.title('Referee EDA')

def page4():
    Player()
    st.sidebar.title('선수 성공 여부 파악')
    st.sidebar.write('좋아하는 선수와 리그 스탯을 통해')
    st.sidebar.write('성공 여부를 알아보세요!')
    st.sidebar.write('(22-23시즌 선수 한정..)')

# 딕셔너리 선언 {  ‘selectbox항목’ : ‘페이지명’ …  }
page_names_to_funcs = {'Main Page': main_page, '리그별 승리 주요 지표':page2,  
                       'Referee EDA': page3, '선수 성공여부 파악': page4}

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox('Select a page', page_names_to_funcs.keys())

# 해당 페이지 부르기
page_names_to_funcs[selected_page]()
