import streamlit as st
import pandas as pd
import requests
from io import StringIO
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("API_URL")

st.title("Custom GPT")

# Initialize chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = requests.post(
        API_URL,
        json={"prompt": prompt}
    ).json()

    if response.get("status") and response.get("data"):
        assistant_response = response["data"]["response"]
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    else:
        st.error("Failed to get response from the server.")
