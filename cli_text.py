import os
import ijson
import json


def has_chinese(s):
    for c in s:
        if "\u4e00" <= c <= "\u9fff":
            return True
    return False


def read_large_json_file(file_path, output_dir, lines_per_file=10000):
    with open(file_path, "rb") as in_file:
        # 使用ijson库的items()方法读取文件内容
        item_count = 0
        file_count = 0
        out_file = open(
            os.path.join(output_dir, f"output_{file_count}.txt"), "w", encoding="utf-8"
        )
        for item in ijson.items(in_file, "item"):
            # 将每个item转换为JSON字符串并打印

            data = json.dumps(item, ensure_ascii=False)[1:][:-1]

            if has_chinese(data):
                out_file.write(data + "\n")

                item_count += 1

            if item_count % lines_per_file == 0:
                out_file.close()
                file_count += 1
                out_file = open(
                    os.path.join(output_dir, f"output_{file_count}.txt"),
                    "w",
                    encoding="utf-8",
                )

        out_file.close()


# 示例：读取一个名为"large_file.json"的大型json文件
read_large_json_file("D:/baidu_download/Refined-Anime-Text.json", "output3")
