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

    def plot_wordcloud(words):
    wc = WordCloud(background_color="white",
                   max_words=1000, font_path="AppleGothic",
                   contour_width=3,
                   colormap='Spectral',
                   contour_color='steelblue')
    wc.generate_from_frequencies(words)
    plt.figure(figsize=(10, 8))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    return plt


def plot_bar(words):
    words_count = Counter(words)
    words_df = pd.DataFrame.from_dict(words_count, orient='index', columns=['count'])
    words_df.sort_values('count', ascending=False, inplace=True)
    ax = words_df.plot(kind='bar', figsize=(10, 4))
    ax.set_title('Top Words')
    ax.set_xlabel('Words')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', labelrotation=45, labelsize=8)
    return ax


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

    st.pyplot(plot_wordcloud(count_top_words))
    st.pyplot(plot_bar(count_top_words))


# 예시 데이터
df = pd.DataFrame({
    'time': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02', '2022-01-03', '2022-01-03'],
    'name': ['a', 'a', 'a', 'b', 'b', 'b'],
    'title+content': ['apple banana', 'apple carrot', 'banana carrot', 'apple banana', 'banana carrot', 'carrot apple']
})

# 사용 예시
get_count_top_words(df, start_date='2022-01-01', last_date='2022-01-03', num_words=3, name='a')
    
    
