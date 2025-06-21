from .base import call_llm, log_journal_entry, get_day_log

def run(date: str):
    memory = "\n".join([entry["content"] for entry in get_day_log(date)])
    prompt = f"Based on this, how would you track mood or well-being trends?"
    tracker = call_llm(prompt)
    log_journal_entry(date, "Wellness Tracker Agent", tracker)
    return tracker
