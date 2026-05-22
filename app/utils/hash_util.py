# 开发时间: 2026/5/22 12:42
import hashlib


def file_md5(file_path: str):

    md5 = hashlib.md5()

    with open(file_path, "rb") as f:

        while True:

            data = f.read(8192)

            if not data:
                break

            md5.update(data)

    return md5.hexdigest()