from .base import call_llm, log_journal_entry, get_day_log

def run(date: str):
    memory = "\n".join([entry["content"] for entry in get_day_log(date)])
    prompt = f"Reflect on this journal entry and summarize the emotions expressed:\n{memory}"
    reflection = call_llm(prompt)
    log_journal_entry(date, "Reflection Agent", reflection)
    return reflection
