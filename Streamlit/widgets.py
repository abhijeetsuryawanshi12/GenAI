import streamlit as st
import pandas as pd

st.title("Streamlit Text input")

name = st.text_input("Enter your name:")

age = st.slider("Select your age")

if name:
    st.write(f"Hello, {name}")

if age:
    st.write(f"Your age is {age}")

options = ["Python","Java","C++","JavaScript"]
choice = st.selectbox("Choose your favourite language:", options)
st.write(f"You selected {choice}")

uploaded_file=st.file_uploader("Choose a csv file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
