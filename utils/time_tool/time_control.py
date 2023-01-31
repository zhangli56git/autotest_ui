import time
from datetime import datetime


# 获取当前时间戳
def get_now_timestamp():
    return int(time.time())


# 获取当前时间 2018-12-12 12:12:12
def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 获取当前时间 格式yyyy-MMdd-HH-mm-ss
def get_now_time_format():
    return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())


# 计算毫秒
def count_milliseconds():
    """
    计算时间
    :return:
    """
    access_start = datetime.now()
    access_end = datetime.now()
    access_delta = (access_end - access_start).seconds * 1000
    return access_delta


# 时间戳转换，将日期格式转换成时间戳
def timestamp_conversion(time_str: str) -> int:
    """
    时间戳转换，将日期格式转换成时间戳
    :param time_str: 时间
    :return:
    """

    try:
        datetime_format = datetime.strptime(str(time_str), "%Y-%m-%d %H:%M:%S")
        timestamp = int(
            time.mktime(datetime_format.timetuple()) * 1000.0
            + datetime_format.microsecond / 1000.0
        )
        return timestamp
    except ValueError as exc:
        raise ValueError('日期格式错误, 需要传入得格式为 "%Y-%m-%d %H:%M:%S" ') from exc


# 时间戳转换成日期
def time_conversion(time_num: int):
    """
    时间戳转换成日期
    :param time_num:
    :return:
    """
    if isinstance(time_num, int):
        time_stamp = float(time_num / 1000)
        time_array = time.localtime(time_stamp)
        other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        return other_style_time


if __name__ == '__main__':

    print(get_now_time_format())
