import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
import koreanize_matplotlib

st.title('한눈에 보는 데이터 프레임')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


df = pd.read_csv('https://raw.githubusercontent.com/seoinhyeok96/BusyPeople/main/data/%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%86%AB%E1%84%83%E1%85%B3_%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%2B%E1%84%82%E1%85%A2%E1%84%8B%E1%85%AD%E1%86%BC.csv')

df['time'] = pd.to_datetime(df['time'])

agree = st.checkbox('밴드')
agree2 = st.checkbox('식물갤러리')



def plot_wordcloud(words):
    wc = WordCloud(background_color="white", 
                   max_words=1000,
                   font_path = "AppleGothic", 
                   contour_width=3, 
                   contour_color='steelblue')
    wc.generate_from_frequencies(words)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")


def plot_bar(words):
    words_count = Counter(words)
    words_df = pd.DataFrame.from_dict(words_count, orient='index', columns=['count'])
    words_df.sort_values('count', ascending=False, inplace=True)
    ax = words_df.plot(kind='bar', figsize=(10, 4))
    ax.set_title('Top Words')
    ax.set_xlabel('Words')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', labelrotation=45, labelsize=8)


def get_tfidf_top_words(df, start_date=None, last_date=None, num_words=10, name=None):
    if name is not None:
        df = df[df['name'] == name]
    if start_date is None:
        start_date = df['time'].min().strftime('%Y-%m-%d')
    if last_date is None:
        last_date = df['time'].max().strftime('%Y-%m-%d')
    df = df[(df['time'] >= start_date) & (df['time'] <= last_date)]
    tfidf_vectorizer = TfidfVectorizer()
    tfidf = tfidf_vectorizer.fit_transform(df['title+content'].values)
    tfidf_df = pd.DataFrame(tfidf.todense(), columns=tfidf_vectorizer.get_feature_names_out())
    tfidf_top_words = tfidf_df.sum().sort_values(ascending=False).head(num_words).to_dict()
    plt.figure(figsize=(12, 6))
    plot_wordcloud(tfidf_top_words)
    plot_bar(tfidf_top_words)
    plt.show()

get_count_top_words(df, '2023-01-01', '2023-02-01', 50, '밴드')





if agree:
    st.write('Great!')
if agree2:
     st.write('식물갤러리')       

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
