from backend.src.utilis.logger import logger
from backend.src.processing.voice_processing import enhance_audio
from backend.src.transcription.speech_text import STTClient

INPUT_AUDIO_PATH = r"C:\Users\lkeja\OneDrive\Desktop\Projects\VoiceGuard\backend\data\test_clip\Testing_sound.wav"
OUTPUT_AUDIO_PATH = r"C:\Users\lkeja\OneDrive\Desktop\Projects\VoiceGuard\backend\data\output\enhanced_audio.wav"

logger.info("Starting Test: Enhance Audio and Transcribe")

enhance_audio(INPUT_AUDIO_PATH, OUTPUT_AUDIO_PATH)
stt = STTClient()
stt.transcribe(OUTPUT_AUDIO_PATH)

logger.info("Test completed: Enhance Audio and Transcribe")