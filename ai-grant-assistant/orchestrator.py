from agents import outline_agent, budget_agent, reviewer_agent
from agents.base import increment_version

def run_agent(agent: str, topic: str, goals="", funding_agency="", scope=""):
    if agent == "Outline":
        return outline_agent.run(topic, goals, funding_agency)
    elif agent == "Budget":
        return budget_agent.run(topic, scope)
    elif agent == "Reviewer":
        return reviewer_agent.run(topic)
    return "Unknown agent."

def next_version(topic: str):
    increment_version(topic)
