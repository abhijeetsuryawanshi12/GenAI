from langchain_community.llms import Ollama
from langchain import PromptTemplate, LLMChain
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant."),
        ("user","Question:""{question}"),
    ]
)

def generate_response(question, engine):
    llm=Ollama(model=engine)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    response = chain.invoke({"question": question})
    return response


# Display the sidebar on streamlit
st.title("QnA Chatbot")

#Side bar settings
st.sidebar.title("Settings")

engine=st.sidebar.selectbox(
    "Select the model",["llama3.2:3b"])

# Adjust response parameters
temparature=st.sidebar.slider(
    "Temparature",
    min_value=0.0,
    max_value=1.0,
    value=0.0,
    step=0.1,
)
max_tokens=st.sidebar.slider(
    "Max Tokens",
    min_value=0,
    max_value=1000,
    value=100,
    step=1,
)


# Get user input
st.write("Go ahead and write your question below:")
question = st.text_input("Enter your question:")

# Generate response
if question:
    response = generate_response(question, engine)
    st.write("Answer:", response)


