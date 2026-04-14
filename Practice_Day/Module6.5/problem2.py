# Problem 2
# Create an app that:
# Takes a prompt from user
# Sends it to Gemini API
# Displays the generated response


from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

prompt = st.text_input("Enter Your Prompt", placeholder="Type here...")
button = st.button("Confirm", type="primary")

if button:
    if prompt:
        with st.spinner("Loading..."):
            Api_Key = os.environ.get("GEMINI_KEY")

            client = genai.Client(api_key=Api_Key)

            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt,
            )

            st.markdown(response.text)
    
    else:
        st.error("Enter a prompt first")