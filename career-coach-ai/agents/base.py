import requests
from tinydb import TinyDB, Query

db = TinyDB("memory/user_store.json")
User = Query()

def call_llm(prompt: str) -> str:
    response = requests.post("http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt, "stream": False})
    return response.json()["response"].strip()

def log_response(username: str, agent: str, session: int, content: str):
    if db.contains(User.name == username):
        db.update(lambda u: u["log"].append({"session": session, "agent": agent, "content": content}), User.name == username)
    else:
        db.insert({"name": username, "session": 1, "log": [{"session": session, "agent": agent, "content": content}]})

def get_user_log(username: str):
    result = db.search(User.name == username)
    return result[0]["log"] if result else []

def increment_session(username: str):
    if db.contains(User.name == username):
        db.update(lambda u: u.update({"session": u["session"] + 1}), User.name == username)

def get_current_session(username: str):
    result = db.search(User.name == username)
    return result[0]["session"] if result else 1
