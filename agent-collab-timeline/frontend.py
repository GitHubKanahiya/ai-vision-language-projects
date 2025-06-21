
import streamlit as st
from timeline import render_timeline

# Existing code...

if st.button("Show Timeline") and topic:
    st.subheader("📈 Agent Collaboration Timeline")
    fig = render_timeline(topic)
    if fig:
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No timeline data available.")
