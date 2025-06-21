
# 🧠 Voice-Controlled Agent System

A local Python-based voice assistant that:
- Accepts voice input
- Converts it to text (via Whisper)
- Processes the input via an AI agent (dummy or GPT)
- Reads the output aloud using Text-to-Speech
- Stores all interaction logs for future reference

## 💻 How to Run

```bash
git clone https://github.com/GitHubKanahiya/voice_agent
cd voice_agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
