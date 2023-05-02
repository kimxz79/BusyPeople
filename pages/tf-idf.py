from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

from wordcloud import WordCloud


df = pd.read_csv('https://raw.githubusercontent.com/seoinhyeok96/BusyPeople/main/data/%ED%8A%B8%EB%A0%8C%EB%93%9C_%EC%A0%9C%EB%AA%A9%2B%EB%82%B4%EC%9A%A9.csv')
df['time'] = pd.to_datetime(df['time'])


def plot_wordcloud(words):
    wc = WordCloud(background_color="white", 
                   max_words=1000,
                   font_path = "AppleGothic", 
                   contour_width=3, 
                   colormap='Spectral', 
                   contour_color='steelblue')
    wc.generate_from_frequencies(words)
    plt.figure(figsize=(10, 8))
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
    
    plt.figure(figsize=(12, 6))
    plot_wordcloud(count_top_words)
    plot_bar(count_top_words)
    plt.show()
    
get_count_top_words(df, '2023-01-01', '2023-02-01', 50, '밴드')
