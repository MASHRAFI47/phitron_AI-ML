# Problem 1
# Create a calculator using Streamlit:
# Two number inputs
# A selectbox for operations (+, -, *, /)
# Display the result when a button is clicked


import streamlit as st

a = st.text_input("Enter first number", placeholder="type any number...")
select = st.selectbox("Enter Operation", ("+", "-", "*", "/"))
b = st.text_input("Enter second number", placeholder="type any number...")

button = st.button("Calculate", type="primary")

if button:
    if a == "" or b == "":
        st.error("Please fill all the inputs")
    else:
        try:
            a = float(a)
            b = float(b)
            
            if select == "+":
                add = a+b
                st.success(add)
            elif select == "-":
                sub = a-b
                st.success(sub)
            elif select == "*":
                mult = a*b
                st.success(mult)
            elif select == "/":
                if b == 0:
                    st.error("Cannot divide with zero")
                else:
                    div = a/b
                    st.success(div)
        except Exception as e:
            st.error(e)