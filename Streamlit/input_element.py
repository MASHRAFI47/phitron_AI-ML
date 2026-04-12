import streamlit as st

st.title("Welcome to input elements", anchor=False)

name = st.text_input("Enter your name", placeholder="Your name")
age = st.number_input("Enter your age", value=None, placeholder="Enter your age")
password = st.text_input("Enter password", placeholder="Enter pass", type="password")

pressed = st.button("Confirm", type="primary")

if pressed:
    st.write("Your Name is:", name)
    st.write("Your Age is:", age)
    st.write("Your Pass is:", password)
    
selected = st.selectbox("Enter your choice", ("Student", "Employee", "Others"), index=None, accept_new_options=True)
st.write("Your type is", selected)