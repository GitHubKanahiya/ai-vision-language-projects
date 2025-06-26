from .base import call_llm, log_response, get_current_version

def run(topic: str, research_goals: str, funding_agency: str):
    prompt = f"Design a detailed grant proposal outline for the topic: {topic}. \
Goals: {research_goals}. Target funding agency: {funding_agency}."
    outline = call_llm(prompt)
    version = get_current_version(topic)
    log_response(topic, "Outline Designer", version, outline)
    return outline
