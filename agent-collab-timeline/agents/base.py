
from datetime import datetime

def log_agent_response(topic: str, agent: str, content: str):
    log_entry = {
        "agent": agent,
        "content": content,
        "timestamp": datetime.now().isoformat()
    }
    if db.contains(Topic.name == topic):
        db.update(lambda t: t["log"].append(log_entry), Topic.name == topic)
    else:
        db.insert({"name": topic, "log": [log_entry]})
