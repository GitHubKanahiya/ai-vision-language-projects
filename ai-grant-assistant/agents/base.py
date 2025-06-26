import requests
from tinydb import TinyDB, Query

db = TinyDB("memory/proposal_store.json")
Proposal = Query()

def call_llm(prompt: str) -> str:
    response = requests.post("http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt, "stream": False})
    return response.json()["response"].strip()

def log_response(topic: str, agent: str, version: int, content: str):
    if db.contains(Proposal.name == topic):
        db.update(lambda p: p["log"].append({
            "version": version,
            "agent": agent,
            "content": content
        }), Proposal.name == topic)
    else:
        db.insert({"name": topic, "version": 1, "log": [{
            "version": version,
            "agent": agent,
            "content": content
        }]})

def get_proposal_log(topic: str):
    result = db.search(Proposal.name == topic)
    return result[0]["log"] if result else []

def increment_version(topic: str):
    if db.contains(Proposal.name == topic):
        db.update(lambda p: p.update({"version": p["version"] + 1}), Proposal.name == topic)

def get_current_version(topic: str):
    result = db.search(Proposal.name == topic)
    return result[0]["version"] if result else 1
