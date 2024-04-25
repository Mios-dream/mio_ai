import requests
import json
from io import BytesIO
import pygame
from init_config import Config
from emotion import emotion_recognition


config = Config()
url = config.gptsovits_url

# 定义一个字典记录不同情绪的参考音频和文字
emotions = {
    "happy": {
        "audio": "emotion_audio/mmn/happy.wav",
        "text": "梦梦奈想要陪阁下过今后的每一个生日",
    },
    "angry": {
        "audio": "emotion_audio/mmn/angry.wav",
        "text": "哼，梦梦奈的手很好玩吗？",
    },
    "disgust": {
        "audio": "emotion_audio/mmn/disgust.wav",
        "text": "笨蛋哥哥。让可爱的妹妹缺少睡眠可是大罪啊",
    },
    "neutral": {
        "audio": "emotion_audio/mmn/neutral.wav",
        "text": "晴朗的天气，要不要出去晒一晒被子呢",
    },
    "awkward": {
        "audio": "emotion_audio/mmn/awkward.wav",
        "text": "阁下，别总是摸呀",
    },
    "question": {
        "audio": "emotion_audio/mmn/question.wav",
        "text": "哼，阁下，怎么了？",
    },
}

# emotions = {
#     "happy": {
#         "audio": "D:/GPT-SoVITS/models/mio/596732.ogg",
#         "text": "老师，欢迎您，你比我预测的早到了43秒。",
#     }
# }

# 初始化系统播发器
pygame.mixer.init()


def tts_text(text: str, **arges) -> None:
    """
    使用gptsovis接口将文字转换为音频，并播放
    @param
        text: 需要播报的文字
            emotion: 情绪，不填将自动识别，可选值：happy, angry, disgust, neutral, awkward, question

    @return: None

    """

    if not arges.get("emotion"):
        emotion = emotion_recognition(text)

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
