import requests
import json
from io import BytesIO


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

# 要合成的语音的情绪
emotion = "happy"


data = {
    "refer_wav_path": emotions[emotion]["audio"],
    "prompt_text": emotions[emotion]["text"],
    "prompt_language": "zh",
    "text": "阁下,最喜欢你啦",
    "text_language": "zh",
    "top_k": 5,
    "top_p": 1,
    "temperature": 1,
}
data = json.dumps(data, ensure_ascii=False)

print(data)

response = requests.post(url, data=data.encode("utf-8"))

# 获取音频数据
audio_data = response.content

# 将音频数据转换为wav文件
audio_data_wav = BytesIO(audio_data)


# 保存wav文件
with open("output.wav", "wb") as f:
    f.write(audio_data_wav.getvalue())
