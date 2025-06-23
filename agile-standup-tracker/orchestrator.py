from agents import summary_agent, blocker_agent, sprint_agent
from agents.base import log_update

def run_agent(agent: str, sprint: str):
    if agent == "Summary":
        return summary_agent.run(sprint)
    elif agent == "Blocker":
        return blocker_agent.run(sprint)
    elif agent == "Sprint":
        return sprint_agent.run(sprint)
    return "Unknown agent."

def submit_update(sprint: str, member: str, update: str):
    log_update(sprint, member, update)
