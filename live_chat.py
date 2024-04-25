import Models.fastgpt_chat_api as fastgpt_chat_api
import Tools.audio as audio
from Models.recognize_whisper import ASR
import os
import time
import threading
import pygame

"""
直接启动即可
实时语音聊天

"""


class stream(threading.Thread):
    # 模拟控制台流式输出
    def __init__(self, response, retaining):
        threading.Thread.__init__(self)
        self.response = response
        self.retaining = retaining

    def run(self):

        # 检测声音是否在播放
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            outdata = ""
            for i in self.response:

                # 输出数据
                outdata += i
                os.system("cls")
                print(self.retaining)
                print("澪：", outdata, "\n")

                # 等待一段时间
                time.sleep(0.2)


class tts(threading.Thread):
    def __init__(self, response):
        threading.Thread.__init__(self)
        self.response = response

    def run(self):
        try:
            audio.tts_text(self.response)
        except Exception as e:
            pass


history = []

# 初始化语音识别模块
asr = ASR(model="medium")

os.system("cls")

print("加载完成")

while True:
    # user_input = input("阁下：")

    print("请阁下说话...")
    user_input = asr.recognize_whisper_from_microphnoe()
    if not user_input:
        continue
    print("阁下：", user_input)
    response = fastgpt_chat_api.chat_fastapi(user_input, history=history)

    history.append({"content": user_input, "role": "user"})

    # print("澪：", response, "\n")

    # 创建新线程
    thread1 = stream(response, "阁下：" + user_input)

    thread2 = tts(response)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
