import json


class Config:

    def __init__(self):
        with open("config.json") as json_file:
            json_data = json.load(json_file)

        self.__dict__ = json_data

        self._set_data(json_data)

    def __str__(self):
        return str(self.__dict__)

    def _set_data(self, json_data):
        # 获取fastgpt相关的配置信息
        self.fastgpt_url = json_data["fastgpt"]["url"]
        self.fastgpt_key = json_data["fastgpt"]["api_key"]

        # 获取gptsovits相关的配置信息
        self.gptsovits_url = json_data["gptsovits"]["url"]
