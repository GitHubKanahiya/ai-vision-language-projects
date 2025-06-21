# 🧠 Mental Health Companion Agents

A journaling + coaching assistant built with autonomous agents and persistent memory to support emotional well-being over time.

## 🛠️ Features

- Daily mood + open journaling
- Reflection Agent: Summarizes emotions
- Cognitive Reframe Agent: Offers new perspectives
- Wellness Tracker Agent: Tracks well-being over time
- Persistent logs with per-date tracking
- Easy-to-use Streamlit frontend

## 🧠 Agents

- **Reflection Agent**: Analyzes mood and summarizes emotional tone
- **Cognitive Reframe Agent**: Offers positive reframes for stressful thoughts
- **Wellness Tracker Agent**: Tracks emotional patterns and trends

## 📂 Project Structure

mental-health-companion/
├── agents/
│ ├── base.py
│ ├── reflection_agent.py
│ ├── reframe_agent.py
│ └── wellness_tracker_agent.py
├── memory/
│ └── mood_log.json
├── orchestrator.py
├── frontend.py
├── requirements.txt
└── README.md


## ▶️ How to Run

1. Install dependencies:

   ```bash
   pip install streamlit tinydb requests

2.Pull model:
ollama pull llama2

3.Start Ollama backend:
ollama run llama2

4.Run the frontend:
streamlit run frontend.py
