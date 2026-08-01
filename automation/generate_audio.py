import os

# تخطي سؤال الموافقة على الترخيص تلقائيًا (ضروري للتشغيل الآلي في GitHub Actions)
os.environ["COQUI_TOS_AGREED"] = "1"

from TTS.api import TTS

SPEAKER_WAV = os.path.join(os.path.dirname(__file__), "speaker_sample.wav")
LANGUAGE = "ar"

_tts = None

def _get_tts():
    global _tts
    if _tts is None:
        _tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
    return _tts

async def make_audio(text, out_path):
    tts = _get_tts()
    tts.tts_to_file(
        text=text,
        speaker_wav=SPEAKER_WAV,
        language=LANGUAGE,
        file_path=out_path,
    )

async def make_scene_audios(scenes, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    paths = []
    for i, text in enumerate(scenes):
        p = os.path.join(out_dir, f"scene_{i}.wav")
        await make_audio(text, p)
        paths.append(p)
    return paths
