import streamlit as st

def referee_insight():
    st.markdown('## 인사이트 도출')
    st.write('#### 1. Laliga와 SerieA의 경우 다른 리그보다 Yellow Card가 많이 나온다.')
    st.write('- 선수들은 몸싸움을 너무 거칠게 하지 않도록 조심해야된다.')
    st.write('#### 2. EPL, Bundesliga는 타 리그에 비해 Red Card가 적다.')
    st.write('- 가설: 감독들이 경고 받은 선수 관리에 더 신경 쓸 것이다.')
    st.write('- 가설: 두 리그의 심판(리그 특성)이 Red카드에 관대할 것이다.')
    st.write('#### 3. 19-20, 20-21 시즌 Fouls/Tackles 값이 증가했다.')
    st.write('- 가설: 모든 리그에서 코로나 시기 선수 보호를 위해 태클을 엄격히 다뤘다.')
    st.write('- 가설: 두 시즌 5개 리그 선수들 모두 거친 몸싸움을 시도했다.')
    st.write('#### 4. EPL의 게임당 파울 횟수가 가장 적다.')
    st.write('- 가설: EPL이 타 리그에 비해 몸싸움에 관대하다.')