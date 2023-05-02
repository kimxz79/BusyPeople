import streamlit as st
import pandas as pd
from streamlit_agraph import agraph, TripleStore

def main():
    st.title('Networkx 그려보자')
    message = st.text_area('키워드를 입력하세요')
    keyword = message
    if st.button('분석하기'):
        st.success(f"{keyword}에 대한 연관어 분석 결과입니다")

if __name__ == '__main__':
    main()

# Define the data
data = [('식물', 'lemon', 8.773420979111814),
        ('식물', '때싹', 8.166747080757542),
        ('식물', '호잇', 8.006354458119853),
        ('식물', '섬광탄', 7.954529050820706),
        ('식물', '개굴', 7.7866337930292415),
        ('식물', '빙고', 7.6275987515220764),
        ('식물', '에스카르고', 7.4945584243029275)]

# Create a triple store from the data
ts = TripleStore()
for row in data:
    ts.add_triple(*row)

# Create the network graph
st.title('Network Graph')
graph = agraph(ts, font_bytes=font_bytes)
st.write(graph)

# Create the network graph
st.title('Network Graph')
agraph(ts)
