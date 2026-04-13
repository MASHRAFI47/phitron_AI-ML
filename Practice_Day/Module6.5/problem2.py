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

