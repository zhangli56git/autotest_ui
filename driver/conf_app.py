from appium import webdriver
from conf.setting import get_yaml_data
from utils.logging_tool.log_control import INFO, ERROR

# 获取driver配置yaml文件路径
conf_driver = get_yaml_data("conf/driver.yaml")


def conf_appium(driver_name):
    """
    配置appium
    :param driver_name:
    :return:
    """
    # 获取driver配置参数
    desired_caps = conf_driver[driver_name]
    INFO.logger.info('{n}:配置文件=>\n{d}'.format(n=driver_name, d=str(desired_caps)))
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    # 判断driver是否为空
    if driver is None:
        ERROR.logger.error(f"driver对象失败=>{driver_name}")
        raise Exception()
    else:
        INFO.logger.info("启动driver对象{}成功!!!【{}】".format(driver_name, driver))
    return driver


if __name__ == '__main__':
    conf_appium("android")
