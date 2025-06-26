from .base import call_llm, log_response, get_current_version

def run(topic: str, estimated_scope: str):
    prompt = f"Create a detailed budget estimate for this grant proposal. Scope: {estimated_scope}."
    budget = call_llm(prompt)
    version = get_current_version(topic)
    log_response(topic, "Budget Estimator", version, budget)
    return budget
