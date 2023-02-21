from selenium import webdriver

from conf.setting import root_path
from utils.logging_tool.log_control import ERROR, INFO

# 获取驱动路径
drivers_path = root_path() + "/files/drivers/"


def conf_webdriver(driver_name) -> webdriver:
    """
    配置webdriver
    :param driver_name:
    :return:
    """
    driver = None
    if driver_name == "chrome":
        driver = webdriver.Chrome(executable_path=drivers_path + "chromedriver")
    elif driver_name == "firefox":
        driver = webdriver.Firefox(executable_path=drivers_path + "geckodriver")
    elif driver_name == "edge":
        driver = webdriver.Edge(executable_path=drivers_path + "MicrosoftWebDriver")
    elif driver_name == "firefoxH5":
        # 启动火狐浏览器h5模式
        profile = webdriver.FirefoxProfile()
        # profile.set_preference("general.useragent.override", conf_driver["firefoxH5"])
        # options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--remote-debugging-port=9222")
        # options.add_argument("--remote-debugging-address=0.0.0.0")
        # options.add_argument("--disable-web-security")
        # page_driver = webdriver.Firefox(executable_path=drivers_path + "geckodriver",options=options)
        # 3.启动浏览器
        driver = webdriver.Firefox(executable_path=drivers_path + "geckodriver", firefox_profile=profile)
        # 判断driver是否为空
    if driver is None:
        ERROR.logger.error("启动:{}失败!!!")
        raise Exception()
    else:
        INFO.logger.info("启动driver对象【{}】成功!!!".format(driver))
        return driver

if __name__ == '__main__':
    conf_webdriver("chrome")
    conf_webdriver("firefox")
    conf_webdriver("edge")
    conf_webdriver("firefoxH5")
