import os
from importlib import import_module
from log import Log
from DataType.MassageData import MassageData


class PluginLoader:
    """
    插件加载器
    """

    # 插件路径
    _plugin_list = os.listdir("Plugin")
    # 插件回调函数字典
    _plugin_recall_list = {}
    # 插件回调函数名列表,用于检查重复
    plugin_name_list = []

    # 加载的插件数量
    plugin_num = 0

    def __init__(self) -> None:
        pass

    def loading(self) -> None:
        """
        加载插件
        """
        for plugin_name in self._plugin_list:
            try:
                # 导入模块
                plugin_model = import_module(f"Plugin.{plugin_name}")

                # 获取优先级
                priority = plugin_model.plugin.setting["priority"]
                # 获取回调函数名
                callback_name = plugin_model.plugin.setting["callback_name"]

                # 检查是否开启插件
                if not plugin_model.plugin.setting["load"]:
                    Log.info(f"插件 {plugin_name} 未开启,跳过加载")
                    continue

                if not hasattr(plugin_model, callback_name):
                    Log.error(
                        f"在加载({plugin_name})时，发现回调函数{callback_name}不存在，请检查回调函数名"
                    )
                    continue

                # 检查是否重复
                if plugin_name in self.plugin_name_list:
                    Log.error(
                        f"在加载{plugin_name}时，发现重复的回调函数名{callback_name},请修改回调函数名,确保其唯一"
                    )
                    continue

                # 将需要回调函数的模块添加到字典中
                self._plugin_recall_list[plugin_model] = priority
                # 记录回调函数名
                self.plugin_name_list.append(callback_name)

                # 记录加载的插件数量
                self.plugin_num += 1

            except Exception as e:
                Log.error(f"加载插件 {plugin_name} 失败，错误信息为: {e}")

        # 按照优先级排序
        self.sorted_dict = dict(
            sorted(
                self._plugin_recall_list.items(), key=lambda item: item[1], reverse=True
            )
        )
        Log.info(f"成功加载了{self.plugin_num}个插件")

    def call_back(self, data: MassageData) -> None:
        """
        调用插件
        """
        for plugin_model in self.sorted_dict.keys():
            # 获取插件名
            plugin_name = plugin_model.plugin.name
            # 获取回调函数名
            callback_name = plugin_model.plugin.setting["callback_name"]
            try:
                # print(f"plugin_model.{callback_name}")
                callback = eval(f"plugin_model.{callback_name}")
                callback(data)

            except Exception as e:
                Log.error(f"调用插件 {plugin_name} 失败，错误信息为: {e}")
