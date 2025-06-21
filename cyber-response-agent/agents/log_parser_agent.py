from agents.base import BaseAgent

class LogParserAgent(BaseAgent):
    def __init__(self):
        super().__init__("Log Parser Agent")

    def run(self, log_data, memory, topic):
        anomalies = []
        for line in log_data.splitlines():
            if "unauthorized" in line.lower() or "failed" in line.lower():
                anomalies.append(line)

        summary = {
            "anomalies_detected": anomalies,
            "total_entries": len(log_data.splitlines()),
            "flagged_entries": len(anomalies)
        }

        memory[topic] = memory.get(topic, {})
        memory[topic]["log_parser"] = summary
        return summary
