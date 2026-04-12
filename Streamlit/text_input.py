import streamlit as st

st.title("My first web", anchor=False)
st.header("Content 1", divider=True)
st.subheader("Content 1")
st.text("Hello world")

st.markdown(":orange-background[:red[**Hello**] *world*] :world_map:")

a = 10
b = 20

st.write(a, b)