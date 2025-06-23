from agents import itinerary_agent, cost_agent, culture_agent

def run_agent(agent: str, topic: str, destination: str = "", budget: str = "", interests: str = ""):
    if agent == "Itinerary":
        return itinerary_agent.run(topic, destination, interests)
    elif agent == "Cost":
        return cost_agent.run(topic, budget)
    elif agent == "Culture":
        return culture_agent.run(topic, destination)
    return "Unknown agent."
