import os
import time


def stream_screen(data: str):
    # 模拟控制台流式输出

    outdata = ""
    for i in data:
        # 输出数据
        outdata += i
        os.system("cls")
        print(outdata)
        # 等待一段时间
        time.sleep(0.2)


stream_screen("阁下你好")
