from bilibili_api import Credential, Danmaku, sync
from bilibili_api.live import LiveDanmaku, LiveRoom
import Models.fastgpt_chat_api as fastgpt_chat_api
import Tools.audio as audio
import os
import time
import threading
import queue


class stream(threading.Thread):
    """
    创建一个线程，用于流式输出文本
    """

    # 模拟控制台流式输出
    def __init__(self, response, retaining):
        threading.Thread.__init__(self)
        self.response = response
        self.retaining = retaining

    def run(self):
        # 直接输出
        os.system("cls")
        print(self.retaining)
        print(self.response)

        # time.sleep(2)
        # outdata = ""
        # for i in self.response:

        #     # 输出数据
        #     outdata += i
        #     os.system("cls")
        #     print(self.retaining)
        #     print("澪：", outdata, "\n")

        #     # 等待一段时间
        #     time.sleep(0.1)


class tts(threading.Thread):
    """
    创建一个线程，用于将文本转换为语音并播放
    """

    def __init__(self, response):
        threading.Thread.__init__(self)
        self.response = response

    def run(self):
        try:
            audio.tts_text(self.response)
        except Exception as e:
            pass


def msg_thread(msg):
    msg_queue.put(msg)


def msg_reply():

    global history, msg_queue
    while True:
        if msg_queue.empty():
            time.sleep(1)
            continue
        msg = msg_queue.get()
        response = fastgpt_chat_api.chat_fastapi(msg, history=history)

        # if len(response) > 70:
        #     response = "澪不想回答这个问题。。。"
        history.append({"content": msg, "role": "user"})

        if len(history) > 6:
            history.pop(0)

        # print("澪：", response)

        # 创建新线程
        thread1 = stream(response, "阁下：" + msg)

        thread2 = tts(response)
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()


history = []
# 消息队列
msg_queue = queue.Queue()


os.system("cls")

print("加载完成")


# 自己直播间号
ROOMID = 31476594
# 凭证 根据回复弹幕的账号填写
credential = Credential(
    sessdata="a8a29d58%2C1726848802%2C176ea%2A31CjCTApmTd5p28EtKjFJBg0CW3I0Qqcv119ZPLeSb2ZuEgIl6kpVO_xfeJJsRs-AuJgISVjMzb2plLWhocWhqVW00T1ZJaUhiN2hrZUlXdEwxT21EX3ZlSXNqV3BMQnJwOVZfQndHWG1NSE9xWVpOY1VJaTZTOGs4VTJOT25GcVdHQXJzRjdBeUdBIIEC",
    bili_jct="abd94b6602d93f3286e01a6bdecc47a1",
    ac_time_value="77b4c5a690ccef8ce8f5fe1a00adc831",
    buvid3="CFDB15EC-E691-C69B-2C0D-F2CCF8B37B7624375-023091611-PxUSHA3pyqb8eJBKsxeM0Q%3D%3D",
)
# 监听直播间弹幕
monitor = LiveDanmaku(ROOMID, credential=credential)
# 用来发送弹幕
sender = LiveRoom(ROOMID, credential=credential)
# 自己的UID 可以手动填写也可以根据直播间号获取
UID = sync(sender.get_room_info())["room_info"]["uid"]

# 创建新线程
thread_msg = threading.Thread(target=msg_reply)
thread_msg.start()


@monitor.on("DANMU_MSG")
async def recv(event):

    # 发送者UID
    uid = event["data"]["info"][2][0]
    # 排除自己发送的弹幕
    # if uid == UID:
    #     return
    # 弹幕文本
    msg = event["data"]["info"][1]
    # if msg[0] == "澪":
    # 发送弹幕
    # await sender.send_danmaku(Danmaku("你好！"))

    # 将消息发送到消息队列
    msg_thread(msg)


# 启动监听
sync(monitor.connect())
