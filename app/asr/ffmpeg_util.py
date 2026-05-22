import platform
import subprocess

from app.utils.path_util import FFMPEG_DIR

def convert_to_wav(input_path: str):

    output_path = input_path + ".wav"

    ffmpeg = get_ffmpeg_path()

    cmd = [
        ffmpeg,
        "-y",
        "-i", input_path,
        "-ac", "1",
        "-ar", "16000",
        output_path
    ]

    subprocess.run(cmd, check=True)

    return output_path

def get_ffmpeg_path():

    system = platform.system().lower()

    machine = platform.machine().lower()

    # windows
    if system == "windows":

        return str(
            FFMPEG_DIR
            / "windows"
            / "x64"
            / "bin"
            / "ffmpeg.exe"
        )

    # linux
    elif system == "linux":

        # arm
        if "aarch64" in machine or "arm" in machine:

            return str(
                FFMPEG_DIR
                / "linux-arm64"
                / "ffmpeg"
            )

        # x64
        return str(
            FFMPEG_DIR
            / "linux-x64"
            / "ffmpeg"
        )

    raise RuntimeError("unsupported system")