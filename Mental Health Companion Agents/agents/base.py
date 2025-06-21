import requests
from tinydb import TinyDB, Query
db = TinyDB("memory/mood_log.json")
Entry = Query()

def call_llm(prompt: str) -> str:
    response = requests.post("http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt, "stream": False})
    return response.json()["response"].strip()

def log_journal_entry(date: str, agent: str, content: str):
    if db.contains(Entry.date == date):
        db.update(lambda e: e["log"].append({"agent": agent, "content": content}), Entry.date == date)
    else:
        db.insert({"date": date, "log": [{"agent": agent, "content": content}]})

def get_day_log(date: str):
    result = db.search(Entry.date == date)
    return result[0]["log"] if result else []
