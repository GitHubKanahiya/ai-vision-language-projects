# ⚖️ Legal Document Analyzer – LexPro

A powerful AI tool that extracts **legal clauses**, **summaries**, and **named entities** from legal documents using LLaMA2 via Ollama.

## 🧠 Features
- Upload or paste full legal documents
- Extract clauses (Termination, Liability, etc.)
- Generate clear, concise summaries
- Identify key entities (names, laws, dates)
- Built using FastAPI + Streamlit

## 🚀 Usage

1. Pull LLaMA2 model via Ollama:
ollama pull llama2
ollama run llama2


2. Run backend:
uvicorn backend.main:app --reload


3. Run frontend:
streamlit run frontend/app.py

---

Need help running it? Let me know if you’d like a [ready-to-use ZIP file](f), a [demo video walkthrough](f), or a [guide to deploy on Hugging Face](f).
