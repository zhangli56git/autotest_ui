"""
selenium 鼠标和键盘操作
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BroActionChains:

    # 初始化
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.action_chains = ActionChains(self.driver)

    # 鼠标悬停
    def move_to_element(self, locator):
        """
        :param locator: 元素定位器
        :return:
        """
        self.action_chains.move_to_element(locator).perform()

    # 鼠标左键单击
    def click(self, locator):
        """
        :param locator: 元素定位器
        :return:
        """
        self.action_chains.click(locator).perform()

    # 鼠标左键双击
    def double_click(self, locator):
        """
        :param locator: 元素定位器
        :return:
        """
        self.action_chains.double_click(locator).perform()

    # 鼠标右键单击
    def context_click(self, locator):
        """
        :param locator: 元素定位器
        :return:
        """
        self.action_chains.context_click(locator).perform()

    # 拖拽
    def drag_and_drop(self, source, target):
        """
        :param source: 源元素定位器
        :param target: 目标元素定位器
        :return:
        """
        self.action_chains.drag_and_drop(source, target).perform()

    # 按住鼠标左键不放
    def click_and_hold(self, locator):
        """
        :param locator: 元素定位器
        :return:
        """
        self.action_chains.click_and_hold(locator).perform()

    # 释放鼠标左键
    def release(self, locator):
        """
        :param locator: 元素定位器
        :return:
        """
        self.action_chains.release(locator).perform()

    # 通过传参模拟键盘按键包括组合
    def key_down(self, key):
        """
        :param key: 键盘按键
        :return:
        """
        self.action_chains.key_down(key).perform()
