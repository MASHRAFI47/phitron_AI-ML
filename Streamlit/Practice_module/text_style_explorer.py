import streamlit as st

name = st.text_input("Enter name", placeholder="your name...")

if name:
    st.title(name)
    st.divider()
    st.header(name)
    st.divider()
    st.subheader(name)
    st.divider()
    st.text(name)