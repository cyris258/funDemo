# 开发时间: 2026/5/22

import os
import uuid
import traceback

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.asr.recognizer import recognize

router = APIRouter()

UPLOAD_DIR = "audio"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/asr")
async def asr(file: UploadFile = File(...)):

    try:

        # 原文件名
        original_name = file.filename

        # 后缀
        suffix = original_name.split(".")[-1]

        # UUID文件名
        filename = f"{uuid.uuid4()}.{suffix}"

        # 保存路径
        save_path = os.path.join(
            UPLOAD_DIR,
            filename
        )

        # 保存上传文件
        with open(save_path, "wb") as f:
            f.write(await file.read())

        # 识别
        result = recognize(save_path)

        return {
            "success": True,
            "message": "识别成功",
            "data": result
        }

    except Exception as e:

        traceback.print_exc()

        return {
            "success": False,
            "message": str(e)
        }