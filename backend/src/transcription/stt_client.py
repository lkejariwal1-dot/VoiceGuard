import whisper


class STTClient:
    def __init__(self):
        self.model = whisper.load_model("tiny")

    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path)
        return result["text"]
