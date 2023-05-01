import wget

import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

from wordcloud import WordCloud

import streamlit as st

font_url = 'https://raw.githubusercontent.com/seoinhyeok96/BusyPeople/main/font/NanumBarunGothic.ttf'

wget.download(font_url)

df = pd.read_csv('https://raw.githubusercontent.com/seoinhyeok96/BusyPeople/main/data/%EC%96%B4%EA%B0%84.csv')

df.columns = ['index','count']

dict_0 = dict(zip(df['index'], df['count']))

# Create and generate a word cloud image:
wc = WordCloud(
    max_font_size=200,
    background_color='white',
    # relative_scaling=0.5,
    width=800,
    height=400,
    font_path='NanumBarunGothic.ttf'
    )
cloud = wc.generate_from_frequencies(dict(dict_0))

fig, ax = plt.subplots(
    figsize=(12,12)
)

# Display the generated image:
plt.imshow(cloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot(fig)

number = st.number_input('Insert a number', min_value=1 , step=1)
bar_df = df[:40]
st.bar_chart(bar_df)
