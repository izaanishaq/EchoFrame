import whisper

# Load Whisper model once
whisper_model = whisper.load_model("small", device="cpu") # Added device="cpu"

def transcribe(audio_path):
    result = whisper_model.transcribe(audio_path)
    return result["text"]
