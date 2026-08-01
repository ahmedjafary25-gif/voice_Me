from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

tts.tts_to_file(
    text="السلام عليكم، ده اختبار للصوت المستنسخ بتاعي.",
    speaker_wav="speaker_sample.wav",
    language="ar",
    file_path="test_output.wav"
)

print("تم! افتح test_output.wav واسمعه")
