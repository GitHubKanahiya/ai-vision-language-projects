
# Acme Product Review Analyzer

AI-powered tool that analyzes customer reviews for sentiment, topic, and summary.

## Features
- Upload CSVs
- Detect sentiment (Positive, Neutral, Negative)
- Extract key topics (e.g., delivery issues)
- Generate short summaries
- Visual dashboard & CSV download

## Stack
- LLM: Mistral via Ollama
- Backend: FastAPI
- Frontend: Streamlit
- Charts: Altair / Matplotlib

## Run Locally
1. `ollama pull mistral`
2. `uvicorn backend.main:app --reload`
3. `streamlit run frontend/app.py`
