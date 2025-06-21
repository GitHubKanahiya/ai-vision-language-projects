
import pyttsx3
import uuid
import os

engine = pyttsx3.init()

def speak_and_save(text):
    filename = f"voice/audio_logs/response_{uuid.uuid4()}.mp3"
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename
