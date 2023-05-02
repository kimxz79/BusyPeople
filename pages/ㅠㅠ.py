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
    ['식물', '몬스테라', '영양제',])

st.write('You selected:', options)


# 파일 업로드를 위한 메시지를 출력합니다.
st.write("CSV 파일을 업로드하세요.")

# 파일 업로드를 받습니다.
uploaded_file = st.file_uploader("")

# 업로드된 파일이 있다면
if uploaded_file is not None:
    # 업로드된 파일을 읽어들입니다.
    df = pd.read_csv(uploaded_file)

    # 읽어들인 데이터를 출력합니다.
    st.write(df)
