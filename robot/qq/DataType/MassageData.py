class MassageData:
    """
    消息数据类
    """

    # QQ号
    QQ = None
    # 昵称
    Nickname = None
    # 机器人QQ号
    Robot = None
    Message = None
    Message_ID = None
    Time = None

    def __str__(self):
        return __dict__
