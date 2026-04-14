from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="give me an idea on CS2 game in 100 words"
)

st.markdown(response.text)