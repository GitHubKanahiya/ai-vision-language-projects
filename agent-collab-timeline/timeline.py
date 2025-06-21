
import plotly.express as px
from tinydb import TinyDB
import pandas as pd

def get_timeline_data(topic):
    db = TinyDB("memory/memory_store.json")
    result = db.search(lambda x: x["name"] == topic)
    if not result:
        return []

    timeline_data = []
    for entry in result[0]["log"]:
        timeline_data.append({
            "Task": entry["agent"],
            "Start": entry["timestamp"],
            "Finish": entry["timestamp"],
            "Description": entry["content"]
        })

    return pd.DataFrame(timeline_data)

def render_timeline(topic):
    df = get_timeline_data(topic)
    if df.empty:
        return None
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Task", hover_data=["Description"])
    fig.update_yaxes(autorange="reversed")
    return fig

fig.write_image(f"timeline_{topic}.png")

