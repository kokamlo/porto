import streamlit as st
from send_mail import send_email
st.header('contanct')

with st.form(key='emial_form'):
    user_email= st.text_input('enter ur email address')
    raw_message = st.text_area('enter ur message')
    message=f"""\
subject:new mail from {user_email}

from: {user_email}
{raw_message}
"""
    button= st.form_submit_button('submit')
    if button:
        send_email(message)
        st.info('u did it !!!!')