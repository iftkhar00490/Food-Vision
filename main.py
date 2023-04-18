import streamlit as st
from loading import predict_and_view
import csv
import os
import pandas as pd

st.markdown("<h1 style='text-align: center'>Food Vision</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: right'><i>BY SHAIKH IFTKHAR AHMED</i></p>", unsafe_allow_html=True)
st.markdown("""---""")
st.write("""
## Food-Vision 101 ##
#### This machine can classify food into different categories! ####
""")
st.markdown("""---""")
buffer = st.file_uploader('upload food image file here', type=['jpg', 'png', 'jpeg'])

try:
  file_details={"filename":buffer.name,"filetype":buffer.type,"filesize":buffer.size}
except AttributeError: 
  st.error("Drop Some file here for your guess to be done")
  st.stop()

if buffer is not None:
  st.write('loading')
  image, name, accuracy = predict_and_view(buffer, r"/acc_model.h5")
  st.image(image, caption=f'prediction is {name} with accuracy {accuracy*100}%')
