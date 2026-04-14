from google import genai
import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

sentence = st.text_input("Enter sentence", placeholder="Type here...")
tone = st.selectbox("select tone", ("formal", "fancy", "professional"), index=None)
button = st.button("Paraphrase", type="primary")


if button:
    if sentence and tone:
        API_KEY = os.environ.get("GEMINI_KEY")

        client = genai.Client(api_key=API_KEY)

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"""
            Improve this sentence professionally.
            Tone: {tone}
            Sentence: "{sentence}"

            Example:
            Input: "i want job"
            Output: "I am seeking a professional opportunity."
            """,
        )
        st.markdown(response.text)
        
    else:
        st.warning("Please select all the fields")

