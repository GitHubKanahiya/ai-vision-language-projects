import streamlit as st
from orchestrator import run_agent, next_version
from tinydb import TinyDB

db = TinyDB("memory/proposal_store.json")
topics = [t["name"] for t in db.all()]

st.title("📄 AI-Powered Grant Proposal Assistant")

topic = st.selectbox("Choose or create a Proposal Topic", options=topics + ["New Topic"])
if topic == "New Topic":
    topic = st.text_input("Enter new proposal topic")

goals = st.text_area("Enter your proposal goals")
funding_agency = st.text_input("Enter target funding agency")
scope = st.text_area("Describe the proposal scope")

agent_choice = st.selectbox("Choose an Agent", ["Outline", "Budget", "Reviewer"])

if st.button("Run Agent") and topic:
    result = run_agent(agent_choice, topic, goals, funding_agency, scope)
    st.subheader(f"{agent_choice} Agent Output")
    st.write(result)

    st.subheader("🧾 Proposal History")
    result = db.search(lambda x: x["name"] == topic)
    if result:
        for entry in result[0]["log"][::-1]:
            st.markdown(f"**v{entry['version']} – {entry['agent']}**: {entry['content']}")

if st.button("📈 Start New Version") and topic:
    next_version(topic)
    st.success("New version started!")
