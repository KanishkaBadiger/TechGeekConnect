# import streamlit as st
# from groq import Groq
# from dotenv import load_dotenv
# import os

# load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")
# if not api_key:
#     st.error("GROQ_API_KEY not found in .env file")
#     st.stop()

# client = Groq(api_key=api_key)

# st.title("🤖 AI Chatbot (Groq – Free API)")

# user_input = st.text_input("Ask me anything:")

# if st.button("Send"):
#     if user_input:
#         response = client.chat.completions.create(
#             model="llama-3.1-8b-instant",  # ✅ UPDATED MODEL
#             messages=[
#                 {"role": "user", "content": user_input}
#             ]
#         )
#         st.markdown("**AI Reply:**")
#         st.write(response.choices[0].message.content)
#     else:
#         st.warning("Please type a question")



import streamlit as st
import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3"  

st.set_page_config(page_title="Ollama Chatbot", page_icon="🤖")

st.title("🤖 Ollama Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]


for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


user_input = st.chat_input("Type your message...")

if user_input:
   
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    payload = {
        "model": MODEL,
        "messages": st.session_state.messages,
        "stream": False
    }

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = requests.post(OLLAMA_URL, json=payload)
            reply = response.json()["message"]["content"]
            st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )