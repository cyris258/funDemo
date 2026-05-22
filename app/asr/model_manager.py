# 开发时间: 2026/5/22 11:32
from pathlib import Path
from funasr import AutoModel

from app.utils.path_util import MODEL_DIR
import os

os.environ["MODELSCOPE_CACHE"] = str(MODEL_DIR)

model = AutoModel(
    model=str(MODEL_DIR / "speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch"),

    punc_model=str(MODEL_DIR / "punc_ct-transformer_cn-en-common-vocab471067-large"),

    vad_model=str(MODEL_DIR / "speech_fsmn_vad_zh-cn-16k-common-pytorch"),

    device="cpu",

    disable_update=True
)