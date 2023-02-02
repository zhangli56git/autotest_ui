"""
配置测试数据
"""
from conf.setting import root_path
import pandas as pd

from utils.logging_tool.log_control import ERROR


# 获取测试数据文件夹地址
def datas_path():
    datas_path = root_path() + "/data"
    return datas_path


# 全文件地址
def get_file_path(file_name):
    file_path = datas_path() + "/" + file_name
    return file_path


# 判断文件是否为Excel文件
def is_excel(file_name):
    if file_name.endswith(".xlsx") or file_name.endswith(".xls"):
        return True
    else:
        return False

# 遍历Excel文所有sheet的
def get_excel_datas(file_name, sheet_name) -> pd.DataFrame:
    file_path = get_file_path(file_name)
    try:
        excel_datas = pd.read_excel(file_path,  sheet_name=sheet_name)
        return excel_datas
    except FileNotFoundError:
        ERROR.logger.error("文件不存在")
    except Exception as e:
        ERROR.logger.error(e)


if __name__ == '__main__':
    # print(get_excel_datas("template.xlsx", "login"))
    # 遍历标题为by_element第一列的所有数据
    for i in get_excel_datas("template.xlsx", "login")["by_element"]:
        print(i)