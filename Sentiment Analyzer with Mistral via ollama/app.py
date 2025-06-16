import streamlit as st
import requests

st.title("Sentiment Analyzer with Mistral")

text = st.text_area("Enter a sentence to analyze:")
if st.button("Analyze Sentiment"):
    response = requests.post("http://127.0.0.1:8000/analyze", data={"text": text})
    sentiment = response.json().get("sentiment", "Unknown")
    st.subheader("Sentiment:")
    st.write(sentiment)
