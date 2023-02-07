import json

import openpyxl
import pandas as pd

from conf.setting import root_path


# 处理定位数据
def json_cl_list(data, key_name) -> list:
    """
    处理定位数据;收取excel单元格str数据转json后获取key和value存list中
    :param data:        json数据
    :param key_name:    json数据中的key
    :return:
    """
    # 判断data是否为空否则报错
    if data is None:
        raise Exception("data is None")
    # 处理data数据
    data = json.loads(data)
    data1 = data[key_name]
    # 判断key_name是否有效
    if data1 is None:
        raise Exception("excel里面的key_name无效")
    data_by = []
    for key, value in data1.items():
        data_by.append(key)
        data_by.append(value)
    # 判断data_by是否为空否则报错
    if data_by is None:
        raise Exception("data_by is None")
    return data_by


class GetExcelDatas:
    """
    获取excel测试数据
    """

    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    # 获取测试数据文件夹地址
    def get_file_path(self):
        """
        获取测试数据文件夹地址
        :return:
        """
        file_path = root_path() + "/data" + "/" + self.file_name
        return file_path

    # 获取sheet页所有数据
    def get_excel_datas_sheet(self) -> pd.DataFrame:
        """
        获取sheet页所有数据
        :return:
        """
        file_path = self.get_file_path()
        excel_datas = pd.read_excel(file_path, sheet_name=self.sheet_name)
        return excel_datas

    # 获取sheet页指定标题下指定行的单元格数据
    def get_excel_datas_call(self, title, index) -> list:
        """
        获取sheet页指定标题下指定行的单元格数据
        :param title:
        :param index:
        :return:
        """
        excel_datas = self.get_excel_datas_sheet()
        call_data = excel_datas[title][index]
        return call_data

    # 获取sheet页多个单元格数据
    def get_excel_datas_calls(self, up, down) -> tuple:
        """
        获取sheet页多个单元格数据，并将复杂list处理成纯tuple
        :param up:
        :param down:
        :return:
        """
        file_path = self.get_file_path()
        wb = openpyxl.load_workbook(file_path)
        sheet = wb[self.sheet_name]
        call_data = []
        for row in sheet[up:down]:
            call_data.append([cell.value for cell in row])
        qwe = json.loads(call_data[0][0])
        list_datas = []
        for key, value in qwe.items():
            list_datas.append(key)
            list_datas.append(value)
            list_datas.append(call_data[0][1])
        return tuple(list_datas)


if __name__ == '__main__':
    get_excel_datas = GetExcelDatas("template.xlsx", "login")
    print(get_excel_datas.get_excel_datas_calls("E2", "F2"))

    # test_data = get_excel_datas.get_excel_datas_call("case_data", 0)
    # print(test_data)
    # print(type(test_data))
    # test_data = json.loads(test_data)
    # list1 = []
    # for key, value in test_data.items():
    #     list1.append(key)
    #     list1.append(value)
    # print(list1)

    #
    # test_data1 = get_excel_datas.get_excel_datas_calls("E2", "F2")
    # print(test_data1)
    # print(type(test_data1))
    # print(test_data1[0][0])
    # print(test_data1[0][1])
    #
    # qwe = json.loads(test_data1[0][0])
    # list = []
    # for key, value in qwe.items():
    #     list.append(key)
    #     list.append(value)
    #     list.append(test_data1[0][1])
    # print(list)
