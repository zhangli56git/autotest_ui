"""
处理Excel文件
"""
import os
import openpyxl
import xlrd as xlrd

from common.setting import ensure_path_sep


# def scan_folder(folder_path):
#     file_info = []
#     for root, dirs, files in os.walk(folder_path):
#         for file_name in files:
#             file_path = os.path.join(root, file_name)
#             file_size = os.path.getsize(file_path)
#             file_info.append((file_name, file_path, file_size))
#     return file_info


def get_excel_data_xlsx(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    workbook.close()
    return data


def get_excel_data_xls(file_path, sheet_name):
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_name(sheet_name)
    data = []
    for row in range(sheet.nrows):
        row_data = sheet.row_values(row)
        data.append(row_data)
    workbook.release_resources()
    return data


def get_excel_test(data_excel: list):
    data_dict = {}
    header_list = []
    excel_list = []
    # 遍历data第一个元素
    for i in range(len(data_excel[0])):
        header_list.append(data_excel[0][i])
    # 遍历data非第一个元素
    for i in range(1, len(data_excel)):
        # 遍历data第二个元素
        for j in range(len(data_excel[i])):
            # 字典存储
            data_dict.update({header_list[j]: data_excel[i][j]})
        # print(data_dict)
        excel_list.append(data_dict.copy())
    return excel_list


class GetExcel:

    # 初始化
    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    # 获取excel数据
    def get_excel_data(self):
        file_path = ensure_path_sep(f"\\data\\{self.file_name}")
        if self.file_name.endswith(".xlsx"):
            return get_excel_data_xlsx(file_path, self.sheet_name)
        elif self.file_name.endswith(".xls"):
            return get_excel_data_xls(file_path, self.sheet_name)
        else:
            raise Exception("文件格式错误")


if __name__ == '__main__':
    datas = GetExcel("demotest.xlsx", "Sheet2").get_excel_data()
    # print(datas)

    data = get_excel_test(datas)
    print(data[0])
    print(data[1])
