from agents import resume_agent, interview_agent, rolefit_agent
from agents.base import increment_session

def run_agent(agent: str, username: str, resume_text="", goal="", role_desc=""):
    if agent == "Resume":
        return resume_agent.run(username, resume_text, goal)
    elif agent == "Interview":
        return interview_agent.run(username, goal)
    elif agent == "RoleFit":
        return rolefit_agent.run(username, resume_text, role_desc)
    return "Unknown agent."

def next_session(username: str):
    increment_session(username)
