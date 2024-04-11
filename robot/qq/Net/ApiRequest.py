import uuid
import json

class RequestApi:
    echo : str
    params : object
    action : str
    def __init__(self, action, args):
        self.echo = uuid.uuid1().__str__()
        self.action = action
        self.params = args


class MessageContext:
    type = "text"
    data : object
    def __init__(self, data):
        self.data = data

class TextSegment:
    type : str
    text : str
    def __init__(self):
        self.type = "text"
        self.text = "测试消息"

segment = TextSegment()
context = MessageContext(segment)
list = [context]
args = RequestApi("send_group_msg", list)
print(json.dumps(args,default=lambda obj: obj.__dict__))