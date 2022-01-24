import streamlit as st
import pickle
st.title('Sentiment Analysis')
test_model=pickle.load(open('model.pkl', rb))
ip=st.text_input('Enter your message')
op=test_model.predict([ip])
if st.button('Predict'):
  st.title(op)
 
