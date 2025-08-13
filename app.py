import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("Shall we talk?")
st.header("AI powered chatbot")

st.sidebar.header("Configure your chatbot")

status = st.sidebar.radio("Model selector",["Gemini-1.5-flash","gpt-4o-mini"])
if status=="Gemini-1.5-flash":
    st.sidebar.success("Selected Gemini-1.5-flash")
elif status=="gpt-4o-mini":
    st.sidebar.success("Selected gpt-4o-mini")

st.sidebar.title("")
key = st.sidebar.text_input("Enter the API_KEY for the selected model:")
keybutton = st.sidebar.button("Use key")
st.sidebar.title("")

with st.form("form"):
    st.subheader("Chat with the bot")
    query = st.text_input("Type here...")
    send = st.form_submit_button("Send")

def gemgenerate(input):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",api_key=key)
    resp = llm.invoke(input)
    st.info(resp.content)
def opgenerate(input):
    llm= ChatOpenAI(model="gpt-4o-mini",api_key=key)
    resp = llm.invoke(input)
    st.info(resp.content)

if keybutton and status=="Gemini-1.5-flash" and not key.startswith("AI"):
    st.sidebar.error("Invalid API-KEY for the selected model")
elif keybutton and status=="gpt-4o-mini" and not key.startswith("sk-"):
    st.sidebar.error("Invalid API-KEY for the selected model")
elif keybutton and status=="gpt-4o-mini" and key.startswith("sk-"):
    st.sidebar.success("API_KEY verified for OpenAI")
elif keybutton and status=="Gemini-1.5-flash" and key.startswith("AI"):
    st.sidebar.success("API_KEY verified for Gemini")

if send and status=="Gemini-1.5-flash" and key.startswith("AI"):
    gemgenerate(query)
elif send and status=="gpt-4o-mini" and key.startswith("sk-"):
    opgenerate(query)


