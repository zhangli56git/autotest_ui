"""
常规设置
"""

import os
from typing import Text

import yaml


def root_path():
    """ 获取 根路径 """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path


def path_sure(path: Text) -> Text:
    """兼容 windows 和 linux 不同环境的操作系统路径 """
    if "/" in path:
        path = os.sep.join(path.split("/"))

    if "\\" in path:
        path = os.sep.join(path.split("\\"))

    return root_path() + path


# 读取appium.yaml文件
def get_yaml_data(file_path: str):
    # 获取yaml文件路径
    yaml_path = path_sure('/') + file_path
    with open(yaml_path, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    # print(get_yaml_data("/conf/appium.yaml"))
    print(get_yaml_data("conf/page_driver.yaml")["android"])