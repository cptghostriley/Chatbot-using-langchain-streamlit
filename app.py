import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

# Streamlit app setup
st.set_page_config(page_title="AI Chatbot", page_icon=":robot_face:", layout="wide")
st.title("AI chatbot using Streamlit and LangChain")
st.header("Let's have a conversation!")

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

st.sidebar.header("Configure your chatbot")

status = st.sidebar.radio("Model selector",["Gemini-1.5-flash","gpt-4o-mini"])
if status=="Gemini-1.5-flash":
    st.sidebar.success("Selected Gemini-1.5-flash")
elif status=="gpt-4o-mini":
    st.sidebar.success("Selected gpt-4o-mini")

st.sidebar.title("")
key = st.sidebar.text_input("Enter the API_KEY for the selected model:", type="password")
keybutton = st.sidebar.button("Use key")
st.sidebar.title("")

# Function to handle API key validation and response generation
def gemgenerate(input):
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",api_key=key)
        resp = llm.invoke(input)
        return resp.content
    except Exception as e:
        return f"Error generating response: {str(e)}"
    
def opgenerate(input):
    try:
        llm = ChatOpenAI(model="gpt-4o-mini",api_key=key)
        resp = llm.invoke(input)
        return resp.content
    except Exception as e:
        return f"Error generating response: {str(e)}"

# API key validation
if keybutton and status=="Gemini-1.5-flash" and not key.startswith("AI"):
    st.sidebar.error("Invalid API-KEY for the selected model")
elif keybutton and status=="gpt-4o-mini" and not key.startswith("sk-"):
    st.sidebar.error("Invalid API-KEY for the selected model")
elif keybutton and status=="gpt-4o-mini" and key.startswith("sk-"):
    st.sidebar.success("API_KEY verified for OpenAI")
elif keybutton and status=="Gemini-1.5-flash" and key.startswith("AI"):
    st.sidebar.success("API_KEY verified for Gemini")


# Chat input and response handling
if prompt := st.chat_input("Type your message..."):
    # Store user's message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate bot response based on selected model and API key
    if status == "Gemini-1.5-flash" and key.startswith("AI"):
        response = gemgenerate(prompt)
    elif status == "gpt-4o-mini" and key.startswith("sk-"):
        response = opgenerate(prompt)
    else:
        response = "Please configure a valid API key in the sidebar first."

    # Store bot's message in session state
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
