import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
from PIL import Image

def Pts_pred_re():
    All_summary = Image.open('../image/All_summary.png')
    All_pred = Image.open('../image/All_pred.png')

    Goals_summary = Image.open('../image/Goals_summary.png')
    Goals_pred = Image.open('../image/Goals_pred.png')

    Assists_summary = Image.open('../image/Assists_summary.png')
    Assists_pred = Image.open('../image/Assists_pred.png')

    SpG_summary = Image.open('../image/SpG_summary.png')
    SpG_pred = Image.open('../image/SpG_pred.png')

    top_3_summary = Image.open('../image/top_3_summary.png')
    top_3_pred = Image.open('../image/top_3_pred.png')

    top_5_summary = Image.open('../image/top_5_summary.png')
    top_5_pred = Image.open('../image/top_5_pred.png')

    Age_summary = Image.open('../image/Age_summary.png')
    Age_pred = Image.open('../image/Age_pred.png')

    st.write('### 모든 지표 사용')
    st.image(All_summary)
    st.image(All_pred)

    st.write('### Goals 사용')
    st.image(Goals_summary)
    st.image(Goals_pred)

    st.write('### Assists 사용')
    st.image(Assists_summary)
    st.image(Assists_pred)

    st.write('### SpG 사용')
    st.image(SpG_summary)
    st.image(SpG_pred)

    st.write('### Top 3 지표 사용')
    st.image(top_3_summary)
    st.image(top_3_pred)

    st.write('### Top 5 지표 사용')
    st.image(top_5_summary)
    st.image(top_5_pred)

    st.write('### Age 사용')
    st.image(Age_summary)
    st.image(Age_pred)