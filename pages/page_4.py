import streamlit as st
import datetime

with st.form(key='profile_form'):
    
    # チェックボックス
    st.title('Jun\'s list')
    st.checkbox('学校に体温の報告')