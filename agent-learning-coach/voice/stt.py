
import whisper
import os
import uuid

model = whisper.load_model("base")

def record_and_transcribe():
    import sounddevice as sd
    from scipy.io.wavfile import write

    fs = 44100
    duration = 5
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    
    filename = f"voice/audio_logs/input_{uuid.uuid4()}.wav"
    write(filename, fs, recording)

    result = model.transcribe(filename)
    return result['text'], filename
