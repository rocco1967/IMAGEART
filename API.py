import openai
import pandas as pd
import streamlit as st
import os
import numpy as np
from PIL import Image
st.header('.....................My name is Ambrose..................')
st.subheader('.............................I^m here to serve you...........................')
st.subheader('I am an advanced neural network specialized in responding in natural language')

st.subheader('To keep the service active make a small donation with PayPal.. Thank you')
st.success('gianfranco.fa@gmail.com')

st.subheader('For use and explanation models read this:')
st.success('https://beta.openai.com/docs/models/overview')
#st.subheader('text-davinci-003.......IS THE ENGINE OF CHATGPT')



##########################################################

###########################################################

#openai.api_key=st.secrets['OPEN_APY_KEY']


    
prompt =st.text_area('YOUR REQUEST:')
openai.api_key=st.secrets['OPEN_APY_KEY']

response = openai.Image.create(prompt=prompt,n=1,
         size="256x256")#top_p=1
#url='gianfranco.fa@gmail.com'
if st.button('RUN'):
    image_url = response['data'][0]['url']
    st.write(image_url)

#st.download_button('download the result on your PC.. After first sloping Run....',(completions.choices[0].text))

