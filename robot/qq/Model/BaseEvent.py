from DataType import GroupMassageData


class BaseEvent(GroupMassageData):
    def __init__(self, data):
        # QQ号
        self.QQ = data.get("user_id")
        # robot的QQ号
        self.Robot = data.get("self_id")
        # 昵称
        self.Nickname = data.get("sender").get("nickname")
        # 群号
        self.Group = data.get("group_id")
        # 群昵称
        self.Group_Nickname = data.get("sender").get("card")
        # 群消息
        self.Message = data.get("message")[0].get("data").get("text")
        # 群消息类型
        self.MessageType = data.get("message")[0].get("type")
        # 消息ID
        self.Message_ID = data.get("message_id")
        # 事件戳
        self.Time = data.get("time")
        # 事件类型
        self.Post_Type = data.get("post_type")

        # 消息类型,private或group
        self.Message_Type = data.get("message_type")
        # 消息子类型
        self.Sub_Type = data.get("sub_type")
