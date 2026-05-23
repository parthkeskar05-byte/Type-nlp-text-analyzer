📝 AI Text Analyzer
Live Demo: type-nlp-text-analyzer-gc02ozalju.streamlit.app
Overview
The AI Text Analyzer is a real-time Natural Language Processing (NLP) web application built by Parth Keskar. Designed with a clean Streamlit interface, this tool utilizes powerful Hugging Face transformer models to process long-form text. It allows users to instantly generate high-quality summaries and classify the emotional sentiment of articles, reviews, or any text block containing at least 30 words.
Key Features
•	Advanced Text Summarization: Condenses large bodies of text into concise, readable summaries using Facebook's state-of-the-art BART-large-CNN model.
•	Real-Time Sentiment Analysis: Classifies text as either POSITIVE or NEGATIVE, complete with a confidence percentage, powered by a fine-tuned DistilBERT model.
•	Smart Resource Caching: Implements Streamlit's @st.cache_resource to load heavy AI models only once, ensuring blazing-fast performance for subsequent queries.
•	Input Validation: Automatically prompts users to provide sufficient context (minimum 30 words) to ensure high-quality AI outputs.
Tech Stack
•	Frontend: Streamlit
•	AI / NLP Backend: Hugging Face transformers library (pipeline)
•	Models Used: * Summarization: facebook/bart-large-cnn
•	Sentiment: distilbert-base-uncased-finetuned-sst-2-english
Local Setup & Installation
To run this project locally on your machine, follow these steps:
	1.	Clone the repository:
https://github.com/parthkeskar05-byte/Type-nlp-text-analyzer
cd Type-nlp-text-analyzer

	2.	Install the required dependencies:
Make sure you have Python installed, then run:
pip install streamlit transformers torch

(Note: PyTorch is required as the underlying backend for the Hugging Face models).
	3.	Run the application:
run app.py

The app will automatically open in your default web browser. Note that the first time you run a query, the application will take a few seconds to download and cache the AI models locally.
