
%%writefile app.py

import streamlit as st
from langchain.llms import OpenAI


# App framework
openai_api_key = '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'
st.write('TAU BT')
prompt = st.text_input('Puch Iss Ki Bhen Ki Aankh')


# stuff to the screen
llm = OpenAI(temperature = 0.9,openai_api_key=openai_api_key)
if prompt:
  response = llm(prompt)
  st.write(response)
