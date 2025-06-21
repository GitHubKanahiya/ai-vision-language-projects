import streamlit as st
import json
from agents.log_parser_agent import LogParserAgent
from agents.threat_intel_agent import ThreatIntelAgent
from agents.containment_agent import ContainmentAdvisorAgent

MEMORY_FILE = "memory/memory_store.json"


def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


st.set_page_config(page_title="CyberSentinel", layout="wide")
st.title("🛡️ CyberSentinel: Cybersecurity Incident Response AI")

st.markdown("Upload suspicious logs, pick a topic, and run intelligent agents to analyze threats.")

# File uploader
uploaded_file = st.file_uploader("Upload Log File", type=["txt", "log"])
log_data = ""
if uploaded_file:
    log_data = uploaded_file.read().decode("utf-8")
    st.text_area("📄 Log Preview", value=log_data, height=200)


topic = st.text_input("🗂️ Incident Topic", value="incident-001")


memory = load_memory()


if st.button("🔍 Run Log Parser Agent"):
    agent = LogParserAgent()
    result = agent.run(log_data, memory, topic)
    st.success("Log Parser Agent executed.")
    st.json(result)
    save_memory(memory)

if st.button("🧠 Run Threat Intel Agent"):
    agent = ThreatIntelAgent()
    result = agent.run(memory, topic)
    st.success("Threat Intel Agent executed.")
    st.json(result)
    save_memory(memory)

if st.button("🚨 Run Containment Advisor Agent"):
    agent = ContainmentAdvisorAgent()
    result = agent.run(memory, topic)
    st.success("Containment Advisor Agent executed.")
    st.json(result)
    save_memory(memory)


st.markdown("---")
if st.checkbox("📋 Show Shared Memory Log"):
    st.json(memory)
