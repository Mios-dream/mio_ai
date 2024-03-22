import requests
import json
from io import BytesIO
import pygame

url = "http://127.0.0.1:9880/"

# 定义一个字典记录不同情绪的参考音频和文字
emotions = {
    "happy": {
        "audio": "emotion_audio/cs.wav",
        "text": "梦梦奈想要陪阁下过今后的每一个生日",
    },
    "sad": {
        "audio": "emotion_audio/cs.wav",
        "text": "梦梦奈想要陪阁下过今后的每一个生日",
    },
    "angry": {
        "audio": "emotion_audio/cs.wav",
        "text": "梦梦奈想要陪阁下过今后的每一个生日",
    },
    "fearful": {
        "audio": "emotion_audio/cs.wav",
        "text": "梦梦奈想要陪阁下过今后的每一个生日",
    },
    "disgusted": {
        "audio": "emotion_audio/cs.wav",
        "text": "梦梦奈想要陪阁下过今后的每一个生日",
    },
    "surprised": {
        "audio": "emotion_audio/cs.wav",
        "text": "梦梦奈想要陪阁下过今后的每一个生日",
    },
}


# 初始化系统播发器
pygame.mixer.init()


def tts_text(text: str, emotion: str = "happy") -> None:
    """
    使用gptsovis接口将文字转换为音频，并播放
    @param
        text: 需要播报的文字
        emotion: 情绪，默认为"happy"
    @return: None

    """

    data = {
        "refer_wav_path": emotions[emotion]["audio"],
        "prompt_text": emotions[emotion]["text"],
        "prompt_language": "zh",
        "text": text,
        "text_language": "zh",
        "top_k": 5,
        "top_p": 1,
        "temperature": 1,
    }
    data = json.dumps(data, ensure_ascii=False)

    # print(data)

    response = requests.post(url, data=data.encode("utf-8"))

    # 获取音频数据
    audio_data = response.content

    # 将音频数据转换为二进制
    audio_data_wav = BytesIO(audio_data)

    # 加载数据，播放声音
    pygame.mixer.music.load(audio_data_wav)
    pygame.mixer.music.play()

    # 检测声音是否在播放
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


# 保存wav文件
# with open("output.wav", "wb") as f:
#     f.write(audio_data_wav.getvalue())
