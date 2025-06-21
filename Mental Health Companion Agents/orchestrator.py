from agents import reflection_agent, reframe_agent, wellness_tracker_agent

def run_agent(agent: str, date: str):
    if agent == "Reflection":
        return reflection_agent.run(date)
    elif agent == "Reframe":
        return reframe_agent.run(date)
    elif agent == "Wellness":
        return wellness_tracker_agent.run(date)
    return "Unknown agent."
