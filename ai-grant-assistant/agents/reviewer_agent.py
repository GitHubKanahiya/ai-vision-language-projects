from .base import call_llm, log_response, get_proposal_log, get_current_version

def run(topic: str):
    logs = get_proposal_log(topic)
    content = "\n".join([f"{l['agent']}: {l['content']}" for l in logs])
    prompt = f"Act like a grant reviewer. Read the following proposal draft and give feedback:\n\n{content}"
    feedback = call_llm(prompt)
    version = get_current_version(topic)
    log_response(topic, "Reviewer Agent", version, feedback)
    return feedback
