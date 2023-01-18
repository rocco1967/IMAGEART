import openai
import pandas as pd
import streamlit as st
import os
import numpy as np
from PIL import Image
import base64
from io import BytesIO

st.subheader('I am an advanced neural network specialized in built IMAGE-ART')

st.subheader('To keep the service active make a small donation with PayPal.. Thank you')
st.success('gianfranco.fa@gmail.com')

st.subheader('For use and explanation models read this:')
st.success('https://beta.openai.com/docs/models/overview')
openai.api_key=st.secrets['OPEN_APY_KEY']
selectbox = st.selectbox(
    "what do you want to process ? IMAGE_ART or IMAGE_VARIATION",
    ("NONE","INSERT_TEXT", "IMAGE_PNG"))
if selectbox == 'INSERT_TEXT':
    prompt=st.text_area('INSERT TEXT')
    response = openai.Image.create(prompt=prompt,n=1,size='1024x1024')
    image_url = response['data'][0]['url']
    st.write(image_url)                                                
if selectbox == 'IMAGE_PNG':
    image=st.file_uploader('UPLOAD FILE',type=['png'])
    response = openai.Image.create_variation(image=image,n=1,size='1024x1024')#(image=open('Cattura.PNG','rb'), n=1, size="256x256")else
    image_url = response['data'][0]['url']
    st.write(image_url)
###############################################################################################################################################################
#openai.api_key=st.secrets['OPEN_APY_KEY']##
#response = openai.Image.create_variation(image=st.file_uploader('carica il file'),n=1,size='256x256')#(image=open('Cattura.PNG','rb'), n=1, size="256x256")
#image=st.file_uploader('UPLOAD FILE',type=['png'])##
#if image is not None:  ##
    #image=image ##
#else:  ##
    #st.warning('UPLOAD FILE PLEASE')  ###
    #st.stop()  ###

#response = openai.Image.create_variation(image=image,n=1,size='1024x1024')#(image=open('Cattura.PNG','rb'), n=1, size="256x256")else  ###


#response = openai.Image.create_variation(image=,n=1,size='256x256')#(image=open('Cattura.PNG','rb'), n=1, size="256x256")
#image=open("Cattura.PNG", "rb")

 
#image_url = response['data'][0]['url']   ###
#st.write(image_url)  ###
