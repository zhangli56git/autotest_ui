"""
二次封装appium里的方法
"""
from telnetlib import EC

from appium.webdriver import WebElement
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from utils.logging_tool.log_control import INFO


# 遍历元素集合，返回一个可见可操作的元素
def get_element(elements: list) -> WebElement:
    """
    :param elements:
    :return: 返回一个可见可操作的元素
    """
    element_is = None
    for element in elements:
        if element.is_displayed() and element.is_enabled():
            element_is = element
    # 判断element不为空和不为list
    if element_is is not None and not isinstance(element_is, list):
        return element_is
    else:
        raise NoSuchElementException("元素不存在")


# 点击元素
def click_element(element: WebElement):
    """
    :param element: 元素
    :return: None
    """
    element.click()


# 忽略元素点击
def click_element_ignore(element: WebElement):
    """
    :param element: 元素
    :return: None
    """
    try:
        element.click()
    except NoSuchElementException:
        INFO.logger.info("元素不存在")


# 获取元素文本值
def get_element_text(element: WebElement):
    """
    :param element: 元素
    :return: 返回元素文本值
    """
    return element.text


# 获取元素属性值
def get_element_attribute(element: WebElement, attribute):
    """
    :param element: 元素
    :param attribute: 属性
    :return: 返回元素属性值
    """
    return element.get_attribute(attribute)


# 输入文本
def send_keys(element: WebElement, text: str) -> None:
    """
    :param element: 元素
    :param text: 输入文本
    :return: None
    """
    element.send_keys(text)


# 清空文本
def clear_text(element: WebElement) -> None:
    """
    :param element: 元素
    :return: None
    """
    element.clear()


# 获取元素坐标
def get_element_location(element: WebElement):
    """
    :param element: 元素
    :return: 返回元素坐标
    """
    return element.location


class ElementDispose:

    # 初始化方法
    def __init__(self, driver):
        self.driver = driver

    # 显示等待元素可见可操作
    def wait_element_visible(self, locator, time=10) -> WebElement:
        """
        :param locator: 元素定位器
        :param time: 等待时间
        :return: 返回元素
        """
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    # 通过字典判断定位方式返回元素集合
    def get_elements_by_dict(self, locator) -> list:
        """
        :param self:
        :param locator: 元素定位器
        :return: 返回元素集合
        """
        by = locator[0]
        value = locator[1]
        if by == "id":
            return self.driver.find_elements_by_id(value)
        elif by == "name":
            return self.driver.find_elements_by_name(value)
        elif by == "xpath":
            return self.driver.find_elements_by_xpath(value)
        elif by == "class":
            return self.driver.find_elements_by_class_name(value)
        elif by == "link_text":
            return self.driver.find_elements_by_link_text(value)
        elif by == "partial_link_text":
            return self.driver.find_elements_by_partial_link_text(value)
        elif by == "tag_name":
            return self.driver.find_elements_by_tag_name(value)
        elif by == "css_selector":
            return self.driver.find_elements_by_css_selector(value)
        else:
            raise NameError("请输入正确的定位方式")

    # 上下左右滑动屏幕
    def swipe_screen(self, direction):
        """
        :param self:
        :param direction: 滑动方向
        :return: None
        """
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        if direction == "up":
            self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4)
        elif direction == "down":
            self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4)
        elif direction == "left":
            self.driver.swipe(width * 3 / 4, height / 2, width / 4, height / 2)
        elif direction == "right":
            self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2)
        else:
            raise Exception("滑动方向错误")

    # 获取元素坐标

    # 拖动元素到指定位置
    def drag_element(self, locator, x, y):
        """
        :param self:
        :param locator: 元素定位器
        :param x: x轴偏移量
        :param y: y轴偏移量
        :return: None
        """
        self.driver.drag_and_drop(self.get_elements_by_dict(locator), x, y)

    # 拖动元素到指定元素
    def drag_element_to_element(self, locator1, locator2):
        """
        :param self:
        :param locator1: 元素1定位器
        :param locator2: 元素2定位器
        :return: None
        """
        self.driver.drag_and_drop(self.get_elements_by_dict(locator1), self.get_elements_by_dict(locator2))