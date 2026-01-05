import streamlit as st
from utils.ollama_helper import get_ai_response

st.set_page_config(page_title = "AI Powered Assistant", layout="wide", page_icon="🤖")

st.title("🤖AI Powered Assistant")

user_input = st.text_input("Ask anything: ")

if st.button("Ask AI"):
    if user_input.strip():
        with st.spinner("AI is thinking..."):
            answer = get_ai_response(user_input)
            st.success(answer)
    else:
        st.warning("Please enter a question")