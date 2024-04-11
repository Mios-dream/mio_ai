from plugins import Plugin


plugin = Plugin(
    auther="三三",
    name="测试插件2",
    version="1.0",
    description="测试插件",
    setting={
        # 加载优先级
        "priority": 1,
        # 插件是否可用启用
        "load": False,
        # 插件回调地址
        "callback_name": "plugin_info",
    },
)


@plugin.register
def plugin_info(a):
    print(a)
    print("插件运行")
