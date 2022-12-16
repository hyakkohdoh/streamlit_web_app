import streamlit as st
from PIL import Image

st.title('サンプルアプリ')
st.caption('これはテストアプリです')

image = Image.open('./data/sample.jpg')
st.image(image, width=200)