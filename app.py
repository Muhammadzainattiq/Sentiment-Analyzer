from transformers import AutoTokenizer, AutoModelForSequenceClassification
import streamlit as st
import torch
import charset_normalizer
from transformers import pipeline
def analyze_sentiment(text):
    # Load the sentiment analysis pipeline
    sentiment_pipeline = pipeline("sentiment-analysis")

    # Analyze sentiment
    result = sentiment_pipeline(text)

    # Extract sentiment label and score
    label = result[0]['label']
    score = result[0]['score']
    return label, score
    # Example usage
text = st.text_input("Enter the text to analyze : ")
if st.button("Analyze"):
  label, score = analyze_sentiment(text)
  # print(f"Sentiment: {label}, Score: {score}")

  st.success(f"Sentiment: {label}")
  st.info(f"Score: {score}")