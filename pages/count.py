import wget
from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

from sklearn.feature_extraction.text import CountVectorizer

from wordcloud import WordCloud

font_url = 'https://raw.githubusercontent.com/seoinhyeok96/BusyPeople/main/font/NanumBarunGothic.ttf'
wget.download(font_url)


df = pd.read_csv('https://raw.githubusercontent.com/seoinhyeok96/BusyPeople/main/data/%ED%8A%B8%EB%A0%8C%EB%93%9C_%EC%A0%9C%EB%AA%A9%2B%EB%82%B4%EC%9A%A9.csv')
df['time'] = pd.to_datetime(df['time'])


def plot_wordcloud(words):
    wc = WordCloud(background_color="white", 
                   max_words=1000,
                   font_path = "NanumBarunGothic.ttf", 
                   contour_width=3, 
                   colormap='Spectral', 
                   contour_color='steelblue')
    return wc.generate_from_frequencies(words)

def plot_bar(words):
    words_count = Counter(words)
    words_df = pd.DataFrame.from_dict(words_count, orient='index', columns=['count'])
    words_df.sort_values('count', ascending=False, inplace=True)
    return words_df
    
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
    return count_top_words
    
df_ = get_count_top_words(df, '2023-01-01', '2023-02-01', 50, '밴드')
barplot = plot_bar(df_)
wordcloud = plot_wordcloud(df_)

fig, ax = plt.subplots(
    figsize=(12,12)
)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

st.bar_chart(barplot)

