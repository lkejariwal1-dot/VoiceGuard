import whisper
import os
from backend.src.utilis.logger import logger

OUTPUT_TEXT_PATH = r"C:\Users\lkeja\OneDrive\Desktop\Projects\VoiceGuard\backend\data\output\speech_text_output.txt"

class STTClient:
    def __init__(self):
        logger.info("Starting STTClient with Whisper model...")
        self.model = whisper.load_model("tiny")

    def transcribe(self, AUDIO_PATH: str) -> None:
        try:
            result = self.model.transcribe(AUDIO_PATH)
            text = result["text"].strip()
            
            # Make sure output directory exists
            os.makedirs(os.path.dirname(OUTPUT_TEXT_PATH), exist_ok=True)
                
            # Write transcription to file
            with open(OUTPUT_TEXT_PATH, "w", encoding="utf-8") as file:
                file.write(text)
                
            logger.info("Transcription completed successfully")

        except Exception:
            logger.exception("Transcription failed")
            raise
            