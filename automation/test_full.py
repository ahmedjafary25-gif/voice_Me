import os, asyncio
from generate_content import generate_unique as generate
from generate_visuals import make_scenes
from generate_audio import make_scene_audios
from build_video import build_long_video

story = generate()
title = story["title"]
scenes = story["scenes"]
print(f"العنوان: {title}")
print(f"عدد المشاهد: {len(scenes)}")

img_paths = make_scenes(scenes, "output/images")
print("تم توليد الصور")

audio_paths = asyncio.run(make_scene_audios(scenes, "output/audio"))
print("تم توليد الصوت بصوتك المستنسخ")

final_path = "output/final_test.mp4"
build_long_video(img_paths, audio_paths, "output/clips", final_path)
print(f"تم! الفيديو جاهز في: {final_path}")
