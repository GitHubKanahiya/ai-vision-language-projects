
from agents.base import BaseAgent

# Dummy known threat indicators
KNOWN_THREATS = ["192.168.1.66", "brute force", "malware", "sql injection"]

class ThreatIntelAgent(BaseAgent):
    def __init__(self):
        super().__init__("Threat Intelligence Agent")

    def run(self, memory, topic):
        anomalies = memory.get(topic, {}).get("log_parser", {}).get("anomalies_detected", [])
        matched_threats = []

        for entry in anomalies:
            for threat in KNOWN_THREATS:
                if threat.lower() in entry.lower():
                    matched_threats.append((entry, threat))

        result = {
            "matched_threats": matched_threats,
            "threat_level": "High" if matched_threats else "Low"
        }

        memory[topic]["threat_intel"] = result
        return result
