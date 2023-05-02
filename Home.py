import streamlit as st

st.set_page_config(page_title='바쁜사람들', layout="wide", initial_sidebar_state="collapsed")

video_file = open('https://youtu.be/n_QOv-nY_zM', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)