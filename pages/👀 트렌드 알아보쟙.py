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

# 2개의 컬럼 생성
col1, col2 = st.beta_columns(2)

# 첫 번째 컬럼에 시작 날짜 입력 위젯 추가
with col1:
    start_date = st.date_input("Start date",
                           value=datetime.today() - timedelta(days=45),
                           min_value=datetime(2022, 4, 27),
                           max_value=datetime(2023, 4, 26))

# 두 번째 컬럼에 끝 날짜 입력 위젯 추가
with col2:
    end_date = st.date_input("End date", 
                         value=datetime.today() - timedelta(days=30),    
                         min_value=datetime(2022, 4, 27),
                         max_value=datetime(2023, 4, 26))

# 선택된 시작 날짜와 끝 날짜 출력
st.write("Selected date range:", start_date, "to", end_date)
