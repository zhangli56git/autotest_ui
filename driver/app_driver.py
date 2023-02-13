# -*- coding: utf-8 -*-
from conf.setting import get_yaml_data
from appium import webdriver

from utils.logging_tool.log_control import INFO, ERROR


def app_conf(platform_name) -> webdriver:
    """
    选择启动app的设备
    :param platform_name:   设备名称
    :return:                webdriver
    """

    # 获取driver配置yaml文件路径
    conf_driver = get_yaml_data("/conf/driver.yaml")

    # 判断app_name
    if platform_name == "android":
        desired_caps = conf_driver["android"]
    elif platform_name == "ios":
        desired_caps = conf_driver["ios"]
    else:
        ERROR.logger.error("设备名称参数错误；{n}".format(n=platform_name))
        raise Exception()

    INFO.logger.info('{n};配置文件=>{d}'.format(n=platform_name, d=str(desired_caps)))

    # 启动appium服务
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    # 判断driver是否启动成功
    if driver:
        INFO.logger.info("启动app成功;driver=>{d}".format(d=driver))
    else:
        ERROR.logger.error("启动app失败")
        raise Exception()

    # 隐式等待5秒
    driver.implicitly_wait(5)

    return driver


if __name__ == '__main__':
    app_conf(platform_name="android")
