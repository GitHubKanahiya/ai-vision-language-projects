import streamlit as st
from orchestrator import run_agent, next_session
from tinydb import TinyDB

db = TinyDB("memory/user_store.json")
users = [u["name"] for u in db.all()]

st.title("💼 Resume & Interview Coach")

username = st.selectbox("Select or add user", options=users + ["New User"])
if username == "New User":
    username = st.text_input("Enter new username")

agent_choice = st.selectbox("Choose an Agent", ["Resume", "Interview", "RoleFit"])

resume_text = st.text_area("Paste your Resume")
career_goal = st.text_input("Career Goal / Target Job")
role_description = st.text_area("Paste Role Description (Only for RoleFit)")

if st.button("Run Agent") and username:
    output = run_agent(agent_choice, username, resume_text, career_goal, role_description)
    st.subheader(f"{agent_choice} Agent Output")
    st.write(output)

    st.subheader("📑 Session History")
    result = db.search(lambda x: x["name"] == username)
    if result:
        for entry in result[0]["log"][::-1]:
            st.markdown(f"**Session {entry['session']} – {entry['agent']}**:\n{entry['content']}")

if st.button("🆕 New Coaching Session") and username:
    next_session(username)
    st.success("New session started.")
