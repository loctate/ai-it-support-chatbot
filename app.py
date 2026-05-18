import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.title("AI IT Support Chatbot")

user_input = st.text_input(
    "Describe your IT issue:"
)

if st.button("Get Solution"):

    prompt = f"""
    You are a professional IT Support technician.

    Help troubleshoot this issue:

    {user_input}

    Give clear step-by-step troubleshooting guidance.
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile"
    )

    answer = response.choices[0].message.content

    st.write(answer)