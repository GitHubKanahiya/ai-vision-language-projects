import streamlit as st
from orchestrator import handle_query
from tinydb import TinyDB

st.title("🧠 Persistent Memory Agent")

db = TinyDB("memory/memory_store.json")
topics = [item["name"] for item in db.all()]
selected_topic = st.selectbox("Choose or create a topic", options=topics + ["Start new topic"])

if selected_topic == "Start new topic":
    selected_topic = st.text_input("Enter new topic name")

user_input = st.text_area("Ask a question or input research note:")

if st.button("Submit") and selected_topic:
    response, history = handle_query(selected_topic, user_input)

    st.subheader("💬 AI Response")
    st.write(response)

    st.subheader("📜 Topic Memory Log")
    for entry in reversed(history):
        st.markdown(f"**You**: {entry['user']}")
        st.markdown(f"**AI**: {entry['ai']}")
