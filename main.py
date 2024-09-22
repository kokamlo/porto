import streamlit as st
import pandas 

st.set_page_config(layout='wide')
col1 , col2 = st.columns(2)
with col1:
    st.image("images/kokamlo.png")

with col2:
    st.title('Behzad hoseinzadeh')
    content=""" i'm behzad , a jonuir python developer """
    st.info(content)

st.write('these are my newbie projects, try not to lough challeng ...')

col3 ,empty_col, col4 = st.columns([1.5, 0.5 , 1.5])

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index , row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f'[click for code]({row["url"]})')

with col4:
    for index , row in df[10:].iterrows():
        st.header(row['title'])    
        st.write(row['description']) 
        st.image("images/" + row['image'])  
        st.write(f'[click for code]({row["url"]})') 