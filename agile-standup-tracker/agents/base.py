import requests
from tinydb import TinyDB, Query

db = TinyDB("memory/sprint_store.json")
Sprint = Query()

def call_llm(prompt: str) -> str:
    response = requests.post("http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt, "stream": False})
    return response.json()["response"].strip()

def log_update(sprint: str, member: str, update: str):
    if db.contains(Sprint.name == sprint):
        db.update(lambda s: s["log"].append({"member": member, "update": update}), Sprint.name == sprint)
    else:
        db.insert({"name": sprint, "log": [{"member": member, "update": update}]})

def get_sprint_log(sprint: str):
    result = db.search(Sprint.name == sprint)
    return result[0]["log"] if result else []
