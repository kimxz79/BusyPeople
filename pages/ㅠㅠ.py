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



df = pd.read_csv('https://raw.githubusercontent.com/seoinhyeok96/BusyPeople/main/data/%ED%8A%B8%EB%A0%8C%EB%93%9C_%EC%A0%9C%EB%AA%A9%2B%EB%82%B4%EC%9A%A9.csv')
df['time'] = pd.to_datetime(df['time'])

def get_count_top_words(df, start_date=None, last_date=None, num_words=10, name=None):
    if name is not None:
        df = df[df['name'] == name]
    if start_date is None:
        start_date = df['time'].min().strftime('%Y-%m-%d')
    if last_date is None:
        last_date = df['time'].max().strftime('%Y-%m-%d')
    df = df[(df['time'] >= start_date) & (df['time'] <= last_date)]
    count_vectorizer = CountVectorizer()
    count = count_vectorizer.fit_transform(df['title+content'].values)
    count_df = pd.DataFrame(count.todense(), columns=count_vectorizer.get_feature_names_out())
    count_top_words = count_df.sum().sort_values(ascending=False).head(num_words).to_dict()
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.write('## Word Cloud')
    plt.figure(figsize=(12, 6))
    plot_wordcloud(count_top_words)
    st.pyplot()
    
    st.write('## Bar Plot')
    plt.figure(figsize=(12, 6))
    plot_bar(count_top_words)
    st.pyplot()
    
    
    def load_data():
    # Load your data using pandas
    # Example:
    df = pd.read_csv('https://raw.githubusercontent.com/seoinhyeok96/BusyPeople/main/data/%ED%8A%B8%EB%A0%8C%EB%93%9C_%EC%A0%9C%EB%AA%A9%2B%EB%82%B4%EC%9A%A9.csv')
    return df
