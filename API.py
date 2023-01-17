import openai
import pandas as pd
import streamlit as st
import os
import numpy as np
from PIL import Image

st.subheader('I am an advanced neural network specialized in built IMAGE-ART')

st.subheader('To keep the service active make a small donation with PayPal.. Thank you')
st.success('gianfranco.fa@gmail.com')

st.subheader('For use and explanation models read this:')
st.success('https://beta.openai.com/docs/models/overview')
#st.subheader('text-davinci-003.......IS THE ENGINE OF CHATGPT')





#openai.api_key=st.secrets['OPEN_APY_KEY']
#####################################################################################################

    
#prompt =st.text_area('YOUR REQUEST:','''None''')
#if prompt=='None' :
  #st.warning('YOUR REQUEST PLEASE')
  #st.stop()
#st.success('Thank your request ')
#openai.api_key=st.secrets['OPEN_APY_KEY']

#response = openai.Image.create(prompt=prompt,n=1,
         #size="256x256")#top_p=1
#url='gianfranco.fa@gmail.com'
#if st.button('RUN'):
    #image_url = response['data'][0]['url']
    #st.write(image_url)

#st.download_button('download the result on your PC.. After first sloping Run....',(completions.choices[0].text))
###########################################################################################################################
#image=st.file_uploader("Choose a file_csv")
image_file = st.file_uploader("Upload an image file", type=["png"])
if image_file is not None:
    input_image = Image.open(image_file)
#prompt=st.image(image,output_format='PNG')

openai.api_key=st.secrets['OPEN_APY_KEY']
response = openai.Image.create_variation(prompt=input_image, n=1, size="256x256")

#image=open("Cattura.PNG", "rb")

 
image_url = response['data'][0]['url']
#for image_url in image_url:
    #st.write(image_url)
st.write(image_url)
