import numpy as np
import soundfile as sf
import json
import os
import re

from app.asr.model_manager import model
from app.asr.ffmpeg_util import convert_to_wav
from app.utils.hash_util import file_md5

CACHE_DIR = "cache"

os.makedirs(CACHE_DIR, exist_ok=True)

def recognize(audio_path: str):
    md5 = file_md5(audio_path)

    cache_file = f"{CACHE_DIR}/{md5}.json"

    # 已存在缓存
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)
    # 转 wav
    wav_path = convert_to_wav(audio_path)

    # 读取音频
    audio, sample_rate = sf.read(wav_path)

    # 双声道 -> 单声道
    if len(audio.shape) > 1:
        audio = np.mean(audio, axis=1)

    # float32
    audio = audio.astype(np.float32)

    # ASR
    result = model.generate(
        input=audio,
        sample_rate=sample_rate
    )

    # 原始结果
    raw = result[0]

    # token
    tokens = raw["text"].split()

    # 时间戳
    timestamps = raw.get("timestamp", [])

    # 分段
    segments = build_segments(tokens, timestamps)

    # 完整文本
    full_text = "".join(tokens)

    with open(
            cache_file,
            "w",
            encoding="utf-8"
    ) as f:

        json.dump(
            result,
            f,
            ensure_ascii=False,
            indent=2
        )

    return {
        "success": True,

        "text": full_text,

        "segments": segments,

        "raw": raw
    }



def build_segments(tokens, timestamps=None):

    text = "".join(tokens)

    # ✔ 统一中文标点
    text = re.sub(r'\s+', '', text)

    # ✔ 按句子切分（核心）
    sentences = re.split(r'(?<=[。！？；])', text)

    segments = []
    segment_id = 1
    start_pos = 0

    for s in sentences:

        if not s.strip():
            continue

        end_pos = start_pos + len(s)

        segments.append({
            "id": segment_id,
            "start": None,   # ⚠ 不再依赖时间
            "end": None,
            "duration": None,
            "text": s
        })

        segment_id += 1
        start_pos = end_pos

    return segments

