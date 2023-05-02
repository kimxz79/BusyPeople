import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
import koreanize_matplotlib
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

st.title('한눈에 보는 데이터 프레임')
agree = st.checkbox('밴드')
agree2 = st.checkbox('식물갤러리')

options = st.multiselect(
    '단어를 선택하세요',
    ['식물', '몬스테라', '영양제', ''],
    ['Yellow', 'Red'])

st.write('You selected:', options)


# 파일 업로드
file = st.file_uploader("https://raw.githubusercontent.com/seoinhyeok96/BusyPeople/main/data/%ED%8A%B8%EB%A0%8C%EB%93%9C_%EC%A0%9C%EB%AA%A9%2B%EB%82%B4%EC%9A%A9.csv", type=["csv"])

# 파일이 업로드된 경우
if file is not None:
    # 업로드한 파일을 pandas 데이터프레임으로 읽기
    df = pd.read_csv(file)
    
    # 데이터프레임 출력
    st.dataframe(df)
    
    # 데이터프레임 정보 출력
    st.write(df.info())
