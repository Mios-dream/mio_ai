# 文本识别表情内容
def emote_content(response):
    jsonstr = []
    # =========== 随机动作 ==============
    # text = ["笑", "不错", "哈", "开心", "呵", "嘻", "画", "欢迎", "搜", "唱"]
    # num = is_array_contain_string(text, response)
    # if num > 0:
    #     press_arry = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    #     press = random.randrange(0, len(press_arry))
    #     jsonstr.append({"content":"happy","key":press_arry[press],"num":num})
    # ===============================

    # =========== 开心 ==============
    text = ["笑", "不错", "哈", "开心", "呵", "嘻", "画", "搜"]
    num = is_array_contain_string(text, response)
    if num > 0:
        jsonstr.append({"content": "happy", "key": "开心", "num": num})
    # =========== 招呼 ==============
    text = ["你好", "在吗", "干嘛", "名字", "欢迎"]
    num = is_array_contain_string(text, response)
    if num > 0:
        press_arry = [
            "招呼",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
        ]
        press = random.randrange(0, len(press_arry))
        jsonstr.append({"content": "call", "key": press_arry[press], "num": num})
    # =========== 生气 ==============
    text = ["生气", "不理你", "骂", "臭", "打死", "可恶", "白痴", "忘记"]
    num = is_array_contain_string(text, response)
    if num > 0:
        jsonstr.append({"content": "angry", "key": "生气", "num": num})
    # =========== 尴尬 ==============
    text = ["尴尬", "无聊", "无奈", "傻子", "郁闷", "龟蛋"]
    num = is_array_contain_string(text, response)
    if num > 0:
        jsonstr.append({"content": "blush", "key": "尴尬", "num": num})
    # =========== 认同 ==============
    text = ["认同", "点头", "嗯", "哦", "女仆", "唱"]
    num = is_array_contain_string(text, response)
    if num > 0:
        jsonstr.append({"content": "approve", "key": "认同", "num": num})
    return jsonstr
