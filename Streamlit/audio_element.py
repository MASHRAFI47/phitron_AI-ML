import streamlit as st

st.title("Audio Output")
st.divider()

st.audio("audio/welcome.mp3", loop=True)

audio_file = st.file_uploader("Enter audio", type=['mp3', 'ogg', 'flac'])

if audio_file:
    st.audio(audio_file)