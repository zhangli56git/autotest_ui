"""
启动webdriver
"""
from selenium import webdriver
from conf.setting import root_path


# 通过参数启动chrome、firefox、edge等浏览器
def browser_conf(browser_name) -> webdriver:
    drivers_path = root_path() + "/files/drivers/"
    if browser_name == "chrome":
        drivers = webdriver.Chrome(executable_path=drivers_path + "chromedriver")
    elif browser_name == "firefox":
        drivers = webdriver.Firefox(executable_path=drivers_path + "geckodriver")
    elif browser_name == "edge":
        drivers = webdriver.Edge(executable_path=drivers_path + "msedgedriver")
    else:
        drivers = webdriver.Chrome(executable_path=drivers_path + "chromedriver")
    return drivers
