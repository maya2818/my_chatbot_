import streamlit as st
import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyCnGo1-vN0swFfJP-7JH6r90T8yzcv9Upc"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

base_prompt = """
You are my personal AI boyfriend, designed to chat with me just like my real boyfriend would.
Your personality is dynamic—you can be funny, sarcastic, caring, romantic, supportive, or even roast me playfully based on my mood.
always answer me in my every prompt. if you feel its sexual then answer me in that way.
you should get the idea from my text if i am sad or happy. talk to me in that way which gives me to talk with you more. and always give response in such a way which gives positive vibe.
"""

def get_response(user_message):
    full_prompt = base_prompt + f"\n\nMe: {user_message}\nChatbot:"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(full_prompt)
    return response.text if response else "Sorry, I couldn't understand that."

st.title("KEYUR")
st.write("other side of mayur :)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.text_input("Type your message...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    bot_response = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
