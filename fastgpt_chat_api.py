import requests
from init_config import Config

config = Config()


# fastapi知识库接口调用-LLM回复
def chat_fastapi(content: str, history: list = [], uid=None, username=None) -> str:
    """
    fastapi知识库接口调用-LLM回复
    @param
        content: 问题
        history: 对话历史
    @return: 回答

    """

    url = config.fastgpt_url

    apikey = config.fastgpt_key

    headers = {"Authorization": f"Bearer {apikey}", "Content-Type": "application/json"}

    history.append({"content": content, "role": "user"})

    # 完整请求
    # timestamp = time.time()
    # data = {
    #     "chatId": timestamp,
    #     "stream": False,
    #     "detail": False,
    #     "variables": {"uid": uid, "name": username},
    #     "messages": [{"content": content, "role": "user"}],
    # }

    # 简化请求
    data = {
        "stream": False,
        "detail": False,
        "messages": history,
    }
    try:
        response = requests.post(
            url, headers=headers, json=data, verify=False, timeout=60
        )

    except Exception as e:
        print(f"【{content}】信息回复异常")
        return "我听不懂你说什么"

    assistant_message = response.json()["choices"][0]["message"]["content"]

    if assistant_message[0:3] == "澪会说":
        assistant_message = assistant_message[3:]

    return assistant_message
