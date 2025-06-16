
from fastapi import FastAPI, Form
import requests

app = FastAPI()

@app.post("/analyze")
def analyze_sentiment(text: str = Form(...)):
    # Replace this with Mistral/Ollama logic
    sentiment = "Positive" if "good" in text else "Negative"
    return {"sentiment": sentiment}
