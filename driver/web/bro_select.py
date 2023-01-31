"""
启动webdriver
"""
from selenium import webdriver
from conf.setting import root_path


# 通过参数启动chrome、firefox、edge等浏览器
def get_driver(browser):
    if browser == "chrome":
        drivers = webdriver.Chrome(executable_path=root_path() + "/files/drivers/chromedriver")
    elif browser == "firefox":
        drivers = webdriver.Firefox(executable_path=root_path() + "/files/drivers/geckodriver")
    elif browser == "edge":
        drivers = webdriver.Edge(executable_path=root_path() + "/files/drivers/msedgedriver")
    else:
        drivers = webdriver.Chrome(executable_path=root_path() + "/files/drivers/chromedriver")
    return drivers
