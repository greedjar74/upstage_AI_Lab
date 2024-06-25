import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

from referee_EDA import referee_EDA
from referee_insight import referee_insight

def referee_main():
    pages = ['Referee EDA 결과', '인사이트 도출']
    selected_page = st.selectbox('페이지를 선택하세요.', pages)

    if selected_page == 'Referee EDA 결과':
        referee_EDA()

    else :
        referee_insight()