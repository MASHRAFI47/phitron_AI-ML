from google import genai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

question = st.text_input("Enter your question", placeholder="type your question...")
button = st.button("Ask", type="primary")

if button:
    if question:
        with st.spinner('Loading...'):
            api_key = os.environ.get("api_key")

            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=question,
            )

            st.markdown(response.text)
    else:
        st.warning("Please type your question first")
