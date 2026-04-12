import streamlit as st

st.title("Video element", anchor=False)
st.divider()

video_file = st.file_uploader("Enter video", type=['mp4', 'mkv'])

button = st.button("Click to upload")

if button:
    if video_file:
        st.video(video_file)
        st.success("File uploaded successfully")
    else:
        st.error("Upload a file first")