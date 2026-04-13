import streamlit as st

audio_file = st.file_uploader("Enter audio", type=['mp3', 'ogg'])
video_file = st.file_uploader("Enter video", type=['mp4', 'mkv'])

button = st.button("Play", type="primary")

if button:
    if not audio_file and not video_file:
        st.error("Please upload one file first")
    else:
        if audio_file:
            st.audio(audio_file)
        
        if video_file:
            st.video(video_file)