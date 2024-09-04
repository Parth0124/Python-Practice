import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")

st.write("This is a text column.")

df= pd.DataFrame({
    'First Column': [1,2,3,4,5],
    'Second Column': [90,80,70,60,50]
})

st.write("The Dataframe is written below:")
st.write(df)

chart_data=pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart(chart_data)
