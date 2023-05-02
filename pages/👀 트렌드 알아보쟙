import warnings
warnings.filterwarnings("ignore", message="PyplotGlobalUseWarning")
import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import ast
from gensim.models import Word2Vec
import time

import streamlit as st
from datetime import datetime, timedelta

# 시작 날짜와 끝 날짜를 선택하는 daterange 위젯 생성
start_date = st.date_input("Start date", datetime.today() - timedelta(days=30))
end_date = st.date_input("End date", datetime.today())

# 선택된 시작 날짜와 끝 날짜 출력
st.write("Selected date range:", start_date, "to", end_date)
