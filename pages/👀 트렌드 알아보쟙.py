import warnings
warnings.filterwarnings("ignore", message="PyplotGlobalUseWarning")

import pandas as pd
import matplotlib.pyplot as plt
import ast
import time

import streamlit as st
from datetime import datetime, timedelta
from streamlit_extras.let_it_rain import rain

rain(
    emoji="🦝",
    font_size=54,
    falling_speed=10,
    animation_length="infinite",
)

# 날짜 선택
col1, col2, col3 = st.beta_columns(3)
with col1:
    start_date = st.date_input("👉🏻 시작 날짜",
                           value=datetime.today() - timedelta(days=45),
                           min_value=datetime(2022, 4, 27),
                           max_value=datetime(2023, 4, 26))
with col2:
    end_date = st.date_input("끝 날짜 👈🏻", 
                         value=datetime.today() - timedelta(days=30),    
                         min_value=datetime(2022, 4, 27),
                         max_value=datetime(2023, 4, 26))
with col3:
    keyword_no = st.number_input("📌 키워드", value=50, min_value=1, step=1)

    
col1, col2 = st.beta_columns(2)
with col1:
    st.write("🗓 ", start_date, "~", end_date)    
with col2:
    st.write(keyword_no, '개의 키워드 선택')
