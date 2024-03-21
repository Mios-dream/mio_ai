import os
import ijson
import json


def has_chinese(str: str) -> bool:
    """
    @due 判断字符串是否存在中文
    @param
        s: 字符串
    @return bool值
    """
    for c in str:
        if "\u4e00" <= c <= "\u9fff":
            return True
    return False


def read_large_json_file(
    file_path: str, output_dir: str, lines_per_file: int = 10000
) -> None:
    """
    @due 对大型json进行分割，保存为text
    @param
        file_path:需要分割的文件路径
        output_dir:输出的文件夹地址
        lines_per_file:保存的每个的文件最大行数
    @return
    """
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


if __name__ == "__main__":
    # 示例：读取一个名为"large_file.json"的大型json文件
    read_large_json_file("D:/baidu_download/Refined-Anime-Text.json", "output3")
