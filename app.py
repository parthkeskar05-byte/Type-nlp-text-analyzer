import streamlit as st
from transformers import pipeline

# 1. Setup the Web App UI
st.set_page_config(page_title="AI Text Analyzer", page_icon="🤖", layout="centered")

st.title("📝 Real-Time NLP Sentiment & Summarization API")
st.write("Built by Parth Keskar | This tool uses Hugging Face transformer models to summarize large texts and classify sentiment.")

# 2. Load the AI Models (Cached so they don't reload every time)
@st.cache_resource
def load_summarizer():
    # Using Facebook's BART model for high-quality summaries
    return pipeline("summarization", model="facebook/bart-large-cnn")

@st.cache_resource
def load_sentiment_analyzer():
    # Using a DistilBERT model for fast sentiment classification
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

with st.spinner("Loading AI Models... (This takes a few seconds on the first run)"):
    summarizer = load_summarizer()
    sentiment_analyzer = load_sentiment_analyzer()

# 3. User Input Section
user_input = st.text_area("Paste a news article, review, or long text here (minimum 50 words):", height=200)

# 4. Processing the Data
if st.button("Analyze Text"):
    if len(user_input.split()) < 30:
        st.warning("⚠️ Please enter at least 30 words for the AI to generate a good summary.")
    else:
        with st.spinner("AI is crunching the numbers..."):
            # Run Summarization
            summary_result = summarizer(user_input, max_length=130, min_length=30, do_sample=False)
            summary_text = summary_result[0]['summary_text']
            
            # Run Sentiment Analysis
            sentiment_result = sentiment_analyzer(user_input)
            sentiment_label = sentiment_result[0]['label']
            sentiment_score = sentiment_result[0]['score']

        # 5. Display the Results
        st.subheader("📌 AI Summary:")
        st.info(summary_text)

        st.subheader("🎭 Sentiment Classification:")
        if sentiment_label == "POSITIVE":
            st.success(f"{sentiment_label} (Confidence: {sentiment_score:.2%})")
        else:
            st.error(f"{sentiment_label} (Confidence: {sentiment_score:.2%})")
