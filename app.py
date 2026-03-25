import streamlit as st
from data_loader import load_data
from model import train_model, chatbot

st.title("📚 arXiv Expert Chatbot")

# load data
@st.cache_data
def load():
    return load_data("sample_data.json")

df = load()

# train once
X, corpus = train_model(df)

# UI
query = st.text_input("Ask your question:")

if st.button("Search"):
    if query:
        answer, context = chatbot(query, X, corpus)

        st.subheader("📖 Answer")
        st.write(answer)

        st.subheader("📄 Paper Summary")
        st.write(context)