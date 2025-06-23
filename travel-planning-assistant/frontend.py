import streamlit as st
from orchestrator import run_agent
from tinydb import TinyDB

db = TinyDB("memory/memory_store.json")
topics = [t["name"] for t in db.all()]

st.title("🌍 Travel Planning Assistant")

topic = st.selectbox("Choose or start a topic", options=topics + ["New Topic"])
if topic == "New Topic":
    topic = st.text_input("Enter new topic name")

agent_choice = st.selectbox("Run agent", ["Itinerary", "Cost", "Culture"])

destination = st.text_input("Enter destination")
budget = st.text_input("Enter your budget (e.g., ₹30,000)")
interests = st.text_area("Enter your interests (e.g., culture, food, nature)")

if st.button("Run Agent") and topic:
    result = run_agent(agent_choice, topic, destination, budget, interests)
    st.subheader(f"{agent_choice} Agent Output")
    st.write(result)

    st.subheader("🧾 Shared Topic Log")
    result = db.search(lambda x: x["name"] == topic)
    if result:
        for entry in result[0]["log"][::-1]:
            st.markdown(f"**{entry['agent']}**: {entry['content']}")
