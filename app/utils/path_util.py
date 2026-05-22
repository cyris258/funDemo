from pathlib import Path
import sys

def get_base_dir():

    # EXE环境
    if getattr(sys, "frozen", False):

        return Path(sys.executable).parent

    # 开发环境
    return Path(__file__).resolve().parent.parent.parent


BASE_DIR = get_base_dir()

MODEL_DIR = BASE_DIR / "models"

CACHE_DIR = BASE_DIR / "cache"

OUTPUT_DIR = BASE_DIR / "output"

FFMPEG_DIR = BASE_DIR / "ffmpeg"