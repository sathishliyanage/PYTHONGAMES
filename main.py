import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sathish liiyanga")
    content = """ I am a 28-year-old Army soldier, dedicated to serving my country with honor and integrity.
    My journey in the military has been filled with challenges that have shaped me into a disciplined and resilient individual. I am committed to the values of duty,
    loyalty, and selfless service, which guide my actions both on and off the battlefield.
In my time in the Army, I've learned the importance of teamwork and camaraderie.
Whether it's during intense training exercises or in the midst of a mission, I can always rely on my fellow soldiers.
We share a bond that goes beyond friendship; it's a brotherhood forged in the crucible of adversity.
My dedication to physical fitness is unwavering.
    """
    st.info(content)
    
content2 = """ Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write('[Source code](https://github.com)')
                
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write('[Source code](https://github.com)')
