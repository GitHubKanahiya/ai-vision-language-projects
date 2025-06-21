from agents.base import BaseAgent

class ContainmentAdvisorAgent(BaseAgent):
    def __init__(self):
        super().__init__("Containment Advisor Agent")

    def run(self, memory, topic):
        threats = memory.get(topic, {}).get("threat_intel", {}).get("matched_threats", [])
        actions = []

        for entry, threat in threats:
            if "192.168." in threat:
                actions.append(f"Block IP address {threat}")
            elif "brute force" in threat:
                actions.append("Lock user account and alert SOC")
            elif "sql injection" in threat:
                actions.append("Sanitize database inputs and audit recent queries")

        if not actions:
            actions.append("No immediate action required. Monitor logs.")

        response = {
            "recommended_actions": actions
        }

        memory[topic]["containment"] = response
        return response
