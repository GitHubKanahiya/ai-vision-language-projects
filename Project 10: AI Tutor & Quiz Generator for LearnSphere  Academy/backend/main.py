
from fastapi import FastAPI, Form
import requests

app = FastAPI()

def query_model(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    return response.json()["response"].strip()

@app.post("/generate/")
def generate_learning_aids(text: str = Form(...)):
    prompts = {
        "explanation": f"Explain this in simple terms for a student:\n\n{text}",
        "quiz": f"Generate 5 quiz questions with answers from this educational content:\n\n{text}",
        "concepts": f"List the key terms or concepts mentioned in this content:\n\n{text}"
    }
    return {k: query_model(p) for k, p in prompts.items()}
