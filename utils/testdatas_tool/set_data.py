import json

from utils.logging_tool.log_control import ERROR


def excel_cell_list(cell_data: list, key_name) -> list:
    """
    处理定位数据;收取excel单元格str数据转json后获取key和value存list中
    :param bl:
    :param cell_data:        json数据
    :param key_name:    json数据中的key
    :return:
    """


    # 将data统一转换为str格式
    cell_data = json.loads(str(cell_data))
    # 处理data数据
    data1 = cell_data[key_name]
    data_by = []
    for key, value in data1.items():
        data_by.append(key_name)
        data_by.append(key)
        data_by.append(value)
    # 判断data_by是否为空否则报错
    if data_by is None:
        ERROR.loggin.error("参数data_by is None={}".format(data_by))
        raise Exception()
    return data_by
