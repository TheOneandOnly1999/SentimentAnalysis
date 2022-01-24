import streamlit as st
st.title('Sentiment Analysis')
import cPickle as pickle
f = open("big_networkx_graph.pickle","rb")
model = f.read()
graph_data = pickle.load(model)
ip=st.text_input('Enter your message')
op=graph_data.predict([ip])
if st.button('Predict'):
  st.title(op)
