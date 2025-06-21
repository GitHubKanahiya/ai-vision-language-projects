
from agents.log_parser_agent import LogParserAgent

agent = LogParserAgent()
response = agent.run(log_data, topic="incident-001")
