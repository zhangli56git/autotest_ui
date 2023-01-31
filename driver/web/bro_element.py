"""
二次封装selenium的元素定位方法
"""

from selenium import webdriver
from selenium.common import NoSuchElementException

from utils.logging_tool.log_control import WARNING, INFO, ERROR


class BroElement:

    # 初始化
    def __init__(self, driver: webdriver):
        self.driver = driver

    # 通过字典判断定位类型返回元素，如果元素不为单个返回列表
    def get_elements(self, locator):
        """
        :param locator: 元素定位器
        :return: 返回元素列表
        """
        if isinstance(locator, dict):
            by = locator["by"]
            value = locator["value"]
            if by == "id":
                return self.driver.find_elements_by_id(value)
            elif by == "name":
                return self.driver.find_elements_by_name(value)
            elif by == "class":
                return self.driver.find_elements_by_class_name(value)
            elif by == "tag":
                return self.driver.find_elements_by_tag_name(value)
            elif by == "link":
                return self.driver.find_elements_by_link_text(value)
            elif by == "partial_link":
                return self.driver.find_elements_by_partial_link_text(value)
            elif by == "xpath":
                return self.driver.find_elements_by_xpath(value)
            elif by == "css":
                return self.driver.find_elements_by_css_selector(value)
            else:
                raise NoSuchElementException("元素定位类型错误")

    # 通过元素列表返回一个可见and可点击的元素
    def get_element(self, locator):
        """
        :param locator: 元素定位器
        :return: 返回元素
        """
        elements = self.get_elements(locator)
        for element in elements:
            if element.is_displayed() and element.is_enabled():
                return element
        return None

    # 点击元素
    def click_element(self, locator):
        """
        :param locator: 元素定位器
        :return: None
        """
        element = self.get_element(locator)
        if element:
            element.click()
        else:
            raise NoSuchElementException("元素定位错误")

    # 忽略元素点击
    def click_element_ignore(self, locator):
        """
        :param locator: 元素定位器
        :return: None
        """
        try:
            self.click_element(locator)
        except NoSuchElementException:
            pass

    # 输入文本
    def input_text(self, locator, text):
        """
        :param locator: 元素定位器
        :param text: 输入文本
        :return: None
        """
        element = self.get_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            raise NoSuchElementException("元素定位错误")

    # 获取元素文本
    def get_text(self, locator):
        """
        :param locator: 元素定位器
        :return: 元素文本
        """
        element = self.get_element(locator)
        if element:
            return element.text
        else:
            raise NoSuchElementException("元素定位错误")

    # 元素拖动
    def drag_element(self, locator, x, y):
        """
        :param locator: 元素定位器
        :param x: x轴偏移量
        :param y: y轴偏移量
        :return: None
        """
        element = self.get_element(locator)
        if element:
            self.driver.drag_and_drop_by_offset(element, x, y)
        else:
            raise NoSuchElementException("元素定位错误")

    # 进入iframe
    def switch_to_iframe(self, locator):
        """
        :param locator: 元素定位器
        :return: None
        """
        element = self.get_element(locator)
        if element:
            self.driver.switch_to.frame(element)
        else:
            raise NoSuchElementException("元素定位错误")

    # 退出iframe
    def switch_to_default_content(self):
        """
        :return: None
        """
        self.driver.switch_to.default_content()
