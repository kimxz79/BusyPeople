import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create some sample text
dict_0 = df['어간'].apply(lambda x: Counter([i[0] for i in eval(x) if i[1] == 'Noun']))[0]
for i in df['어간'].apply(lambda x: Counter([i[0] for i in eval(x) if i[1] == 'Noun']))[1:]:
    dict_0 = dict_0 + i

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
