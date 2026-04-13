import streamlit as st

name = st.text_input("Enter Name")
age = st.number_input("Enter age", value=None)
occupation = st.selectbox("Choose profession", ("Student", "Employee", "Businessman", "Freelancer"), index=None, accept_new_options=True)

button = st.button("Click to confirm", type="primary")

if button:
    if name and age and occupation:
        st.write(f"Your name is {name}")
        st.write(f"Your age is {age}")
        st.write(f"Your occupation is {occupation}")
        st.success("Congrats")
    else:
        st.warning("Please fill all the info")