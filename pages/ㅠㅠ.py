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


df = pd.read_csv('https://raw.githubusercontent.com/seoinhyeok96/BusyPeople/main/data/%ED%8A%B8%EB%A0%8C%EB%93%9C_%EC%A0%9C%EB%AA%A9%2B%EB%82%B4%EC%9A%A9.csv')
    
def plot_wordcloud(df,words):
    wc = WordCloud(background_color="white", 
                   max_words=1000,font_path = "AppleGothic", 
                   contour_width=3, 
                   colormap='Spectral', 
                   contour_color='steelblue')
    wc.generate_from_frequencies(words)
    plt.figure(figsize=(10, 8))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")   
    


    
    
