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
st.subheader('text-davinci-003.......IS THE ENGINE OF CHATGPT')


model_engine = st.radio(
    "CHOOSE THE MODEL OF A.I.",
    ('None','text-ada-001','text-davinci-002', 'text-davinci-003', 'code-davinci-002','code-cushman-001','text-curie-001'))
##########################################################
#name = st.text_input('Name')
if model_engine=='None' :
  st.warning('CHOSE A MODEL')
  st.stop()
st.success('Thank you for chose a Model')
###########################################################

openai.api_key=st.secrets['OPEN_APY_KEY']


    
prompt =st.text_area('YOUR REQUEST:')

completions = openai.Completion.create(engine=model_engine,prompt=prompt,max_tokens=1024,n=1, stop=None,
                                      frequency_penalty=0.0,temperature=0.0,)#top_p=1

if st.button('RUN'):
    message =(completions.choices[0].text)#
    st.write(message)

st.download_button('download the result on your PC.. After first sloping Run....',(completions.choices[0].text))

