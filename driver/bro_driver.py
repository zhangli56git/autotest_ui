from selenium import webdriver

from conf.setting import get_yaml_data, root_path
from utils.logging_tool.log_control import INFO


def bro_conf(bro_name) -> webdriver:
    """
    选择启动浏览器的设备
    :param bro_name:    浏览器名称
    :return:            webdriver
    """
    # 获取driver配置yaml文件路径
    conf_driver = get_yaml_data("/conf/driver.yaml")

    # 获取驱动路径
    drivers_path = root_path() + "/files/drivers/"

    # 判断app_name
    if bro_name == "chrome":
        drivers = webdriver.Chrome(executable_path=drivers_path + "chromedriver")
    elif bro_name == "firefox":
        drivers = webdriver.Firefox(executable_path=drivers_path + "geckodriver")
    elif bro_name == "edge":
        drivers = webdriver.Edge(executable_path=drivers_path + "MicrosoftWebDriver")
    elif bro_name == "firefoxH5":
        # 启动火狐浏览器h5模式
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", conf_driver["firefoxH5"])
        # options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--remote-debugging-port=9222")
        # options.add_argument("--remote-debugging-address=0.0.0.0")
        # options.add_argument("--disable-web-security")
        # driver = webdriver.Firefox(executable_path=drivers_path + "geckodriver",options=options)
        # 3.启动浏览器
        drivers = webdriver.Firefox(executable_path=drivers_path + "geckodriver", firefox_profile=profile)
    else:
        raise Exception("浏览器名称参数错误；" + bro_name)

    # 判断driver是否启动成功
    if drivers:
        INFO.logger.info("启动浏览器成功;driver=>{d}".format(d=drivers))
    else:
        raise Exception("启动浏览器失败")

    # 隐式等待5秒
    drivers.implicitly_wait(5)
    return drivers
