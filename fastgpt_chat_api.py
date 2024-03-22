import requests

import time

import audio

history = [{"role": "user", "content": "你叫什么名字"}]


# fastapi知识库接口调用-LLM回复
def chat_fastapi(content, uid, username):

    url = "https://localhost:3020/api/v1/chat/completions"

    apikey = "fastgpt-FNOKqGwbhXPIgfP6uCsr1PlO60zeeU3wWucoT2FcfE66fba9XY23Rjrp"

    headers = {"Authorization": f"Bearer {apikey}", "Content-Type": "application/json"}

    timestamp = time.time()

    data = {
        "chatId": timestamp,
        "stream": False,
        "detail": False,
        "variables": {"uid": uid, "name": username},
        "messages": [{"content": content, "role": "user"}],
    }
    try:
        response = requests.post(
            url, headers=headers, json=data, verify=False, timeout=60
        )
    except Exception as e:
        print(f"【{content}】信息回复异常")
        return "我听不懂你说什么"
    assistant_message = response.json()["choices"][0]["message"]["content"]
    return assistant_message


chat_fastapi("你好", "12", "wqe")
