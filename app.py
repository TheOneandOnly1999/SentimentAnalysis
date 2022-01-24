import streamlit as st
import pickle
st.title('Sentiment Analysis')
filename = 'finalized_model.sav'
test_model= pickle.load(open(filename, 'rb'))
ip=st.text_input('Enter your message')
op=test_model.predict([ip])
if st.button('Predict'):
  st.title(op)
