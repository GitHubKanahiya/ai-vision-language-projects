# Persistent Memory Agent System 🧠

An AI assistant that remembers conversations and research topics across sessions.

## ✨ Features
- Topic-specific memory persistence
- Continue from where you left off
- Uses LLaMA2 locally via Ollama
- Lightweight memory with TinyDB
- Streamlit-based simple UI

## 🚀 How to Run (Windows)
1. **Install Python** and dependencies  
2. **Install Ollama** from [https://ollama.com/download](https://ollama.com/download)  
3. Pull model:
    ```bash
    ollama pull llama2
    ```
4. Start Ollama in background:
    ```bash
    ollama run llama2
    ```
5. Run the app:
    ```bash
    streamlit run frontend.py
    ```
