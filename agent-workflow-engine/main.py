from voice.stt import record_and_transcribe
from voice.tts import speak_and_save
from agent_orchestrator import run_agent
import json
import os

MEMORY_FILE = "memory/memory_store.json"

def save_memory(query, response):
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([], f)

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    data.append({"user": query, "agent": response})
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def main():
    user_input, input_audio = record_and_transcribe()
    print("You said:", user_input)

    response = run_agent(user_input)
    print("Agent:", response)

    output_audio = speak_and_save(response)

    save_memory(user_input, response)

if __name__ == "__main__":
    main()
