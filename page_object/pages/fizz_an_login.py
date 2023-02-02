"""
bobaAN登录步骤页
"""
from driver.app.app_helper import *


class LoginStep:

    # 初始化
    def __init__(self, driver: ElementDispose):
        self.driver = driver

    # 手机登录步骤
    def phone_step(self, by_datas, phone, code):
        click_element()
        self.driver.cli