import websockets
import json
from init_config import Config
from log import Log
from Model.BaseEvent import BaseEvent

from plugin_loader import PluginLoader


class OneBotReceive:
    plugin = None

    def __init__(self, config: Config) -> None:

        self.config = config

    async def Start(self):
        self.Websocket = await websockets.connect(self.config.Websocket)
        Log.info("websockets连接成功")
        self.plugin = PluginLoader()
        self.plugin.loading()
        await self.Receive()

    async def Receive(self):
        while True:
            context = await self.Websocket.recv()
            if not context.isspace():
                obj = json.loads(context)
                # 输出收到的消息到控制台
                Log.adapter(obj)

                # 处理消息
                MessageData = BaseEvent(obj)
                self.plugin.call_back(MessageData)
