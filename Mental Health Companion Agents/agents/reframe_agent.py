from .base import call_llm, log_journal_entry, get_day_log

def run(date: str):
    memory = "\n".join([entry["content"] for entry in get_day_log(date)])
    prompt = f"Reframe the following journal in a positive and empowering way:\n{memory}"
    reframed = call_llm(prompt)
    log_journal_entry(date, "Cognitive Reframe Agent", reframed)
    return reframed
