打包命令

pyinstaller run.py --name FunASR_Service --onedir --clean --collect-all torch --collect-all torchaudio --collect-all funasr --collect-all modelscope --collect-all jieba --collect-all uvicorn --collect-all fastapi --collect-all starlette --collect-all numpy

页面测试地址
http://127.0.0.1:5010/docs#/default/asr_asr_post