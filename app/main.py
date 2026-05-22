# 开发时间: 2026/5/22

from fastapi import FastAPI

from app.api.asr_api import router as asr_router

app = FastAPI(
    title="FunASR Service",
    version="1.0"
)

app.include_router(asr_router)