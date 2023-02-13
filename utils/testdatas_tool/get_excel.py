import json

import openpyxl
import pandas as pd

from conf.setting import root_path
from utils.logging_tool.log_control import INFO, ERROR, DEBUG


class GetExcel:
    """
    获取excel测试数据
    """

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_path = root_path() + "/data" + "/" + file_name

    def get_excel_sheet(self, sheet_name) -> pd.DataFrame:
        """
        获取sheet页数据
        :param sheet_name:  sheet页名称
        :return:        sheet页数据
        """
        data_excel = pd.read_excel(self.file_path, sheet_name=sheet_name)
        return data_excel

    # 获取sheet页指定单元格数据
    def get_excel_sheet_cells(self, sheet_name, up, down) -> list:
        """
        获取sheet页数据单元格数据
        :param sheet_name:  sheet页名称
        :param up:          起始行
        :param down:        结束行
        :return:
        """
        wb = openpyxl.load_workbook(self.file_path)
        sheet = wb[sheet_name]
        # 获取单元格数据
        call_data = []
        for row in sheet[up:down]:
            call_data.append([cell.value for cell in row])
        if up == down:
            INFO.logger.info("\n获取单个cell数据=>{}".format(call_data[0][0]))
            return call_data[0][0]
        else:
            INFO.logger.info("\n获取多个cell数据=>{}".format(call_data))
            return call_data


if __name__ == '__main__':
    get_excel = GetExcel(file_name="test_data.xlsx")
    data = get_excel.get_excel_sheet_cells(sheet_name="login", up='D2', down='D2')
    # data转json
    data = json.loads(str(data))
    # 遍历data
    for key, value in data.items():
        print("key=>{k};value=>{v}".format(k=key, v=value))
        if key in '点击':
            print("点击")
        elif key in '输入':
            print("输入")
