from typing import Tuple
from DataType.GroupMassageData import GroupMassageData
import asyncio


class MessageApi:
    def __init__(self, websocket) -> None:
        self.websocket = websocket

    async def sendGroupMessage(
        self, message: Tuple[str | list], data: GroupMassageData
    ):
        # 实现发送消息的逻辑
        api = "send_group_msg"

        data = {
            "action": api,
            "params": {
                "group_id": data.Group,
                "message": {"type": "text", "data": {"text": message}},
            },
            "echo": "",
        }
        await self.websocket.send(data)
