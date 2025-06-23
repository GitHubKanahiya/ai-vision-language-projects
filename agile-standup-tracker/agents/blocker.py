from .base import call_llm, get_sprint_log

def run(sprint: str):
    log = get_sprint_log(sprint)
    updates = "\n".join([u["update"] for u in log])
    prompt = f"Detect blockers or issues in the following standup updates:\n\n{updates}"
    return call_llm(prompt)
