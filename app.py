import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load Environment Variables
load_dotenv()

# Load Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
)

# Page Configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Amogh's Introduced AI Chatbot")
st.caption("Powered by LangChain + Google Gemini")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
prompt = st.chat_input("Ask anything...")

if prompt:

    # Save User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):
            response = llm.invoke(prompt)

            st.markdown(response.content)

    # Save AI Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.content
        }
    )