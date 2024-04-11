from pydantic import BaseModel


class GroupMassageData(BaseModel):
    # QQ号
    QQ: int
    # robot的QQ号
    Robot: int
    # 昵称
    Nickname: str
    # 群号
    Group: int
    # 群昵称
    Group_Nickname: str
    # 群消息
    Message: str
    # 群消息类型
    MessageType: str
    # 消息ID
    Message_ID: str
    # 事件戳
    Time: str
    # 事件类型
    Post_Type: str

    # 消息类型,private或group
    Message_Type: str
    # 消息子类型
    Sub_Type: str
