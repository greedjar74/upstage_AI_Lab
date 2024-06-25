import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

from feature_BL import feature_BL
from feature_EPL import feature_EPL
from feature_LL import feature_LL
from feature_L1 import feature_L1
from feature_SA import feature_SA
from feature_Big5 import feature_Big5
from Pts_pred_re import Pts_pred_re
from feature_insight import feature_insight

def feature_main():
    leagues = ['Bundesliga', 'EPL', 'Laliga', 'Ligue1', 'SerieA', '5대 리그 통합', '승리 예측 모델', '인사이트 도출']
    selected_league = st.selectbox('리그를 선택하세요', leagues)

    if selected_league == 'Bundesliga':
        feature_BL()

    elif selected_league == 'EPL':
        feature_EPL()

    elif selected_league == 'Laliga':
        feature_LL()

    elif selected_league == 'Ligue1':
        feature_L1()

    elif selected_league == 'SerieA':
        feature_SA()

    elif selected_league == '5대 리그 통합':
        feature_Big5()

    elif selected_league == '승리 예측 모델':
        Pts_pred_re()

    else :
        feature_insight()