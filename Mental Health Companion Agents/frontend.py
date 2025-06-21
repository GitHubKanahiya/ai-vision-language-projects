import streamlit as st
from orchestrator import run_agent
from tinydb import TinyDB
from datetime import date

db = TinyDB("memory/mood_log.json")
st.title("🧘‍♀️ Mental Health Companion")

today = str(date.today())
st.subheader("Today's Entry")
mood = st.selectbox("How are you feeling today?", ["🙂 Good", "😐 Okay", "🙁 Sad", "😤 Stressed", "😢 Down"])
journal = st.text_area("Write freely about your day...")

if st.button("Save Entry"):
    db.insert({"date": today, "log": [{"agent": "User", "content": f"Mood: {mood}\n{journal}"}]})
    st.success("Journal entry saved!")

st.subheader("Run a Companion Agent")
agent_choice = st.selectbox("Choose Agent", ["Reflection", "Reframe", "Wellness"])
if st.button("Run Agent"):
    result = run_agent(agent_choice, today)
    st.subheader(f"{agent_choice} Agent Output")
    st.write(result)

st.subheader("📖 Past Logs")
log = db.search(lambda e: e["date"] == today)
if log:
    for entry in log[0]["log"][::-1]:
        st.markdown(f"**{entry['agent']}**: {entry['content']}")
