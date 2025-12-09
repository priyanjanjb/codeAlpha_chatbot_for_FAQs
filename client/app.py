import sys
import os 
import pandas as pd
import streamlit as st

#Root directory
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

#import backend 
from server.model import get_best_answer

# ✅ Page config must be FIRST streamlit call
st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="./assets/chatbotIcon.png"
)

st.title("🤖 FAQ Chatbot")

# ✅ Chat storage
if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

# ✅ INPUT FORM
with st.form(key="chat_form", clear_on_submit=True):

    user_input = st.text_input("Ask a question")
    submitted = st.form_submit_button("Send")


# ✅ CHAT PROCESSING
if user_input and submitted:
    answer = get_best_answer(user_input)

    st.session_state.messages.append({
        "user": user_input,
        "bot": answer
    })
    
    st.session_state["user_input"] = ""

# ✅ Show chat history
for chat in st.session_state.messages:
    st.markdown(f"**You:** {chat.get('user')}")
    st.markdown(f"**Bot:** {chat.get('bot')}")
    st.markdown("---")
