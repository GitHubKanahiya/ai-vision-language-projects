
# 💼 Earnings Call Analyzer (Mistral + Ollama)

An AI-powered assistant to analyze earnings call transcripts and generate concise summaries, sentiment classification, and actionable financial insights.

## 🔍 Features
- 🔹 Summary in 3 lines
- 🔹 Sentiment classification (Positive, Neutral, Negative)
- 🔹 Extracted insights (growth, risks, guidance)
- 🔹 Streamlit frontend + FastAPI backend
- 🔹 Powered by Mistral via Ollama

## 🚀 Run Locally

### Prerequisites:
- Python 3.8+
- [Ollama](https://ollama.com/)
- `pip install -r requirements.txt`

### Steps:
1. Pull model: `ollama pull mistral`
2. Start backend: `uvicorn backend.main:app --reload`
3. Start frontend: `streamlit run frontend/app.py`

## 📁 Project Structure
earnings-call-analyzer/
├── backend/
│ └── main.py
├── frontend/
│ └── app.py
├── data/
│ └── tesla_q4_2024.txt
├── requirements.txt
└── README.md