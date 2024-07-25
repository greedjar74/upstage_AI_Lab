import streamlit as st
import json
import requests

st.title('basic calculate app')

option = st.selectbox('연산을 선택하세요',
                      ('add', 'sub', 'mul', 'div'))
st.write('')
st.write('숫자를 선택하세요')
x = st.slider('x', 0, 100, 20)
y = st.slider('y', 0, 130, 10)

inputs = {'operation': option, 'x':x, 'y':y}

if st.button('calculate'):
    res = requests.post(url='http://127.0.0.1:8000/calculate', data=json.dumps(inputs))

    st.subheader(f'response form api = {res.text}')