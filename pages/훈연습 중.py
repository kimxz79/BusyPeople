import streamlit as st
import pandas as pd
from streamlit_agraph import agraph, TripleStore
import wget

font_url = 'https://raw.githubusercontent.com/seoinhyeok96/BusyPeople/main/font/NanumBarunGothic.ttf'
wget.download(font_url)

# Define the data
data = [('식물', 'lemon', 8.773420979111814),
        ('식물', '때싹', 8.166747080757542),
        ('식물', '호잇', 8.006354458119853),
        ('식물', '섬광탄', 7.954529050820706),
        ('식물', '개굴', 7.7866337930292415),
        ('식물', '빙고', 7.6275987515220764),
        ('식물', '에스카르고', 7.4945584243029275)]

# Create a triple store from the data
ts = TripleStore(font_path='NanumBarunGothic.ttf')
for row in data:
    ts.add_triple(*row)

# Create the network graph
st.title('Network Graph')
agraph(ts)
