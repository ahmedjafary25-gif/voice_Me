import time
from TTS.api import TTS

t0 = time.time()
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
t1 = time.time()
print(f"وقت تحميل الموديل: {t1-t0:.2f} ثانية")

tts.tts_to_file(
    text="السلام عليكم، ده اختبار للصوت المستنسخ بتاعي.",
    speaker_wav="speaker_sample.wav",
    language="ar",
    file_path="test_output1.wav"
)
t2 = time.time()
print(f"وقت توليد المشهد الأول: {t2-t1:.2f} ثانية")

tts.tts_to_file(
    text="هذه جملة ثانية مختلفة تمامًا لاختبار سرعة التوليد المتكرر.",
    speaker_wav="speaker_sample.wav",
    language="ar",
    file_path="test_output2.wav"
)
t3 = time.time()
print(f"وقت توليد المشهد الثاني: {t3-t2:.2f} ثانية")
