import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Adarsh Manjunath")
    content = '''An Amateur programmer who wants learn to program effectively and efficiently.'''
    st.info(content)

contact_me = '''Below you can find the apps I built while learning Python. Feel free to contact me!'''
st.write(contact_me)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

#displays 0-10 rows in column3
with col3:
    for index, row in df[:10].iterrows():
        st.title(row["title"])

#displays 10-20 rows in column4
with col4:
    for index, row in df[10:].iterrows():
        st.title(row["title"])