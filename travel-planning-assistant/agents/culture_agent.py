from .base import call_llm, log_agent_response, get_topic_log

def run(topic: str, destination: str):
    memory = "\n".join([m["content"] for m in get_topic_log(topic)])
    prompt = f"Give cultural tips, etiquette, and local do's/don'ts for {destination}.\n\n{memory}"
    culture = call_llm(prompt)
    log_agent_response(topic, "Culture Coach Agent", culture)
    return culture
