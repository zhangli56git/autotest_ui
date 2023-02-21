import json

from utils.logging_tool.log_control import ERROR


def list_bys(cell_data: list, key_name) -> list:
    """
    处理定位数据;收取excel单元格str数据转json后获取key和value存list中
    :param cell_data:   excel单元格数据
    :param key_name:    定位方式
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


def list_datas(cells_data: list) -> list:
    """
    处理excel中测试数据和预期结果
    :param cells_data:
    :return:
    """
    datas = []
    # 遍历cells_data
    for i in cells_data:
        # 处理测试数据
        case_data = json.loads(i[0])
        # 处理预期结果
        case_expect = i[1]
        # 处理测试数据和预期结果
        data = []
        for key, value in case_data.items():
            data.append(key)
            data.append(value)
        data.append(case_expect)
        datas.append(data)
    return datas
