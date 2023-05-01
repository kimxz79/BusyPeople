import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

DATE_COLUMN = '어간'
DATA_URL = ('https://raw.githubusercontent.com/seoinhyeok96/BusyPeople/main/data/%EC%96%B4%EA%B0%84%EB%8D%B0%EC%9D%B4%ED%84%B0.csv')

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data_load_state = st.text('Loading data...')
df = load_data()
data_load_state.text("Done! (using st.cache_data)")

dict_0 = dict(zip(df['index'], df['0']))

# Create and generate a word cloud image:
wc = WordCloud(
    max_font_size=200,
    background_color='white',
    # relative_scaling=0.5,
    width=800,
    height=400,
    font_path='/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
    )
cloud = wc.generate_from_frequencies(dict(dict_0))

fig, ax = plt.subplots(
    figsize=(12,12)
)

# Display the generated image:
plt.imshow(cloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()
