from .base import call_llm, get_sprint_log

def run(sprint: str):
    log = get_sprint_log(sprint)
    updates = "\n".join([f"{u['member']}: {u['update']}" for u in log])
    prompt = f"Summarize today's standup updates:\n\n{updates}"
    return call_llm(prompt)
