import streamlit as st
from orchestrator import run_agent, submit_update
from tinydb import TinyDB

db = TinyDB("memory/sprint_store.json")
sprints = [s["name"] for s in db.all()]

st.title("🚀 Agile Standup Assistant")

sprint = st.selectbox("Choose or create a Sprint", options=sprints + ["New Sprint"])
if sprint == "New Sprint":
    sprint = st.text_input("Enter new sprint name")

member = st.text_input("Your Name")
update = st.text_area("Your Standup Update")

if st.button("Submit Update") and member and update:
    submit_update(sprint, member, update)
    st.success("Update logged!")

agent_choice = st.selectbox("Run an AI Agent", ["Summary", "Blocker", "Sprint"])
if st.button("Run Agent") and sprint:
    output = run_agent(agent_choice, sprint)
    st.subheader(f"{agent_choice} Agent Output")
    st.write(output)

    st.subheader("📜 Sprint Log")
    result = db.search(lambda x: x["name"] == sprint)
    if result:
        for entry in result[0]["log"][::-1]:
            st.markdown(f"**{entry['member']}**: {entry['update']}")
