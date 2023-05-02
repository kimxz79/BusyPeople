import streamlit as st

st.set_page_config(page_title='바쁜사람들', layout="wide", initial_sidebar_state="collapsed")

video_file = open('https://pixabay.com/videos/id-45961/', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)