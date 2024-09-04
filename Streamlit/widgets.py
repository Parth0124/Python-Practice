import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name=st.text_input("Enter your name:")

age=st.slider("Select your age:", 0,100,25)

options = ["python", "Java", "C++", "C"]
choice = st.selectbox("choose your fav language", options)

if name:
    st.write(f"Hello {name}")

st.write(f"Your age is {age}")

st.write(f"Your favouriate language is: {choice}")

data={
    "Name": ["John", "Jane", "Jake"],
    "Age": [56,34,45],
    "City":["Pune", "New York","Chicago"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_files=st.file_uploader("Choose a CSV file", type='csv')
if uploaded_files is not None:
    df=pd.read_csv(uploaded_files)
    st.write(df)

