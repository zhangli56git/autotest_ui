import os

import yaml
from selenium import webdriver

from conf.setting import get_yaml_data

# 获取appium.yaml文件中的数据
data = get_yaml_data("/conf/appium.yaml")


# 启动appium服务
def appium_conf(appium: str):
    desired_caps = {}
    if appium == "android":
        desired_caps = data["object_android"]
    if appium == "ios":
        desired_caps = data["object_ios"]
    '''
    {
        'platformName': data['platformName'],
        'platformVersion': data['platformVersion'],
        'deviceName': data['deviceName'],
        'appPackage': data['appPackage'],
        'appActivity': data['appActivity'],
        'unicodeKeyboard': data['unicodeKeyboard'],
        'resetKeyboard': data['resetKeyboard'],
        'noReset': data['noReset'],
        'automationName': data['automationName'],
        'newCommandTimeout': data['newCommandTimeout'],
        'app': data['app']
    }
    '''
    # Appium server URL
    appium_url = data['APPIUM_URL']
    driver = webdriver.Remote(appium_url, desired_caps)
    return driver
