# 🤖 AI Vision-Language Projects

A curated collection of **AI-powered applications** that combine **computer vision** and **natural language processing**. This repository serves as a hub for experimenting with **multimodal AI**, where models can understand both images and text.

---

## 📌 What This Repo Contains

This repository includes multiple projects and experiments that involve:

- 🖼️ Image Understanding  
- 📝 Caption Generation  
- ❓ Visual Question Answering  
- 📋 Document Parsing & Summarization  
- 🧠 Real-time Vision-Language Interaction  

Each project is built using a modular approach with clean separation of backend, frontend, and model logic. Most projects use **LLaVA via Ollama**, **FastAPI**, and **Streamlit**.

---

## 🛠 Tech Stack

| Tool/Library       | Purpose                                |
|--------------------|----------------------------------------|
| 🧠 Ollama + LLaVA   | Vision-Language Model Execution        |
| ⚙️ FastAPI          | Backend API for model communication    |
| 🎨 Streamlit        | Interactive User Interfaces            |
| 🐍 Python           | Core logic and data handling           |
| 📦 Pillow/Requests  | Image I/O and HTTP utilities           |

---

## 📂 Typical Project Structure

Each project is organized like this:

project-name/
├── backend/ # FastAPI app to handle requests
│ └── main.py
├── frontend/ # Streamlit app for UI
│ └── app.py
├── requirements.txt # Python dependencies
└── README.md # Project-specific readme


## 🚀 How to Run Any Project (Locally on Windows)

1. **Clone this repository**
   ```bash
   git clone https://github.com/GitHubKanahiya/ai-vision-language-projects.git
   cd ai-vision-language-projects
   
2. Navigate into a project folder
   cd project-name
Set up a virtual environment



3.Set up a virtual environment
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt



4.Start the model via Ollama
ollama pull llava
ollama run llava

5.Run the backend
uvicorn backend.main:app --reload

6.Run the frontend
streamlit run frontend/app.py


🔭 Goals of This Repository
Demonstrate real-world use cases of multimodal AI

Create reusable templates for AI-based apps

Build an open-source playground for vision-language models

Educate and showcase possibilities with tools like Ollama, LLaVA, Streamlit, and FastAPI

📬 Contributing
Want to contribute your own multimodal AI project?
Feel free to fork, clone, and submit a pull request!

📖 License
This repository is licensed under the MIT License.

🙌 Acknowledgments
LLaVA

Ollama

Streamlit

FastAPI













