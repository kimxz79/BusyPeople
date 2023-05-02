import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

def main():
    # 폰트 설정
    plt.rc('font', family='NanumGothic')

    st.title('Networkx 그려보자')
    message = st.text_area('키워드를 입력하세요')
    keyword = message
    if st.button('분석하기'):
        st.success(f"{keyword}에 대한 연관어 분석 결과입니다")

        # Define the data
        data = [('식물', 'lemon', 8.773420979111814),
                ('식물', '때싹', 8.166747080757542),
                ('식물', '호잇', 8.006354458119853),
                ('식물', '섬광탄', 7.954529050820706),
                ('식물', '개굴', 7.7866337930292415),
                ('식물', '빙고', 7.6275987515220764),
                ('식물', '에스카르고', 7.4945584243029275)]

        # Create the network graph
        G = nx.DiGraph()
        for row in data:
            G.add_edge(row[0], row[1], weight=row[2])

        pos = nx.spring_layout(G)

        labels = {}
        for edge in G.edges(data=True):
            if edge[2]['weight'] > 8:
                labels[(edge[0], edge[1])] = edge[2]['weight']

        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
        nx.draw_networkx_labels(G, pos, font_size=12, font_family='NanumGothic', font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12, font_family='NanumGothic')

        plt.axis('off')
        st.pyplot()

if __name__ == '__main__':
    main()

