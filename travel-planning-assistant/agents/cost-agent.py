from .base import call_llm, log_agent_response, get_topic_log

def run(topic: str, budget: str):
    memory = "\n".join([m["content"] for m in get_topic_log(topic)])
    prompt = f"Estimate the cost of the planned trip with a budget of {budget}. Use any relevant data:\n{memory}"
    cost = call_llm(prompt)
    log_agent_response(topic, "Cost Estimator Agent", cost)
    return cost
