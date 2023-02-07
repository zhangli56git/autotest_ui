# -*- coding: utf-8 -*-
from conf.setting import get_yaml_data
from appium import webdriver

from utils.logging_tool.log_control import INFO, ERROR


def app_conf(device_name) -> webdriver:
    """
    启动app
    :param device_name:
    :return:
    """

    print("\n")

    INFO.logger.info(
        """
                         _    _         _      _____         _
          __ _ _ __ (_)  / \\  _   _| |_ __|_   _|__  ___| |_
         / _` | '_ \\| | / _ \\| | | | __/ _ \\| |/ _ \\/ __| __|
        | (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
         \\__,_| .__/|_/_/   \\_\\__,_|\\__\\___/|_|\\___||___/\\__|
              |_|
              启动【" + device_name + "】app中...
            """
    )


    # 获取app配置yaml文件路径
    conf_data = get_yaml_data("/conf/appium.yaml")
    # 判断app_name
    if device_name == "android":
        desired_caps = conf_data["android"]
        INFO.logger.info("配置文件=====>\n" + str(desired_caps))
    elif device_name == "ios":
        desired_caps = conf_data["ios"]
        INFO.logger.info("配置文件=====>\n" + str(desired_caps))
    else:
        raise Exception("设备名称参数错误；" + device_name)

    # 启动appium服务
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    # 判断driver是否为空
    if driver is None:
        ERROR.logger.info("启动【" + device_name + "】app失败！！！")
    INFO.logger.info("启动【" + device_name + "】app成功！！！")
    driver.implicitly_wait(10)
    return driver


if __name__ == '__main__':
    app_conf(device_name="android")
