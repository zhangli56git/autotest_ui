"""
二次封装appium里的方法
"""
import time

from selenium.common import NoSuchElementException

from utils.logging_tool.log_control import INFO


class AppiumHelper:

    # 初始化方法
    def __init__(self, driver):
        self.driver = driver


# 强制等待3秒
def sleep(self):
    time.sleep(3)


# 显示等待元素可见
def wait_element_visible(self, locator, s: int):
    """
    :param self:
    :param locator: 元素定位器
    :param s: 等待时间
    :return: 返回元素
    """
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    return WebDriverWait(self.driver, s).until(EC.visibility_of_element_located(locator))


# 隐式等待5秒
def wait(self, s: int):
    self.driver.implicitly_wait(s)


# 通过字典判断定位方式
def get_element_by_dict(self, locator):
    """
    :param self:
    :param locator: 元素定位器
    :return: 返回元素
    """
    by = locator["by"]
    value = locator["value"]
    if by == "id":
        return self.driver.find_element_by_id(value)
    elif by == "xpath":
        return self.driver.find_element_by_xpath(value)
    elif by == "name":
        return self.driver.find_element_by_name(value)
    elif by == "class":
        return self.driver.find_element_by_class_name(value)
    elif by == "tag":
        return self.driver.find_element_by_tag_name(value)
    elif by == "link":
        return self.driver.find_element_by_link_text(value)
    elif by == "partial_link":
        return self.driver.find_element_by_partial_link_text(value)
    else:
        raise Exception("定位方式错误")


# 判断元素是否存在并打印到控制台并且返回这个元素
def is_element_exist(self, locator):
    """
    :param self:
    :param locator: 元素定位器
    :return: 返回元素
    """
    try:
        self.get_element_by_dict(locator)
        INFO("元素存在")
        return True
    except NoSuchElementException:
        INFO("元素不存在")
        return False


# 获取一个元素列表。遍历出可操作和可见元素
def get_elements(self, locator):
    """
    :param self:
    :param locator: 元素定位器
    :return: 返回元素列表
    """
    elements = self.get_element_by_dict(locator)
    return [element for element in elements if element.is_displayed() and element.is_enabled()]


# 点击元素
def click_element(self, locator):
    """
    :param self:
    :param locator: 元素定位器
    :return: None
    """
    self.get_element_by_dict(locator).click()


# 忽略元素点击
def click_element_ignore(self, locator):
    """
    :param self:
    :param locator: 元素定位器
    :return: None
    """
    try:
        self.get_element_by_dict(locator).click()
    except NoSuchElementException:
        INFO.logger("元素不存在" + locator)


# 获取元素文本值
def get_element_text(self, locator):
    """
    :param self:
    :param locator: 元素定位器
    :return: 返回元素文本值
    """
    return self.get_element_by_dict(locator).text


# 获取元素属性值
def get_element_attribute(self, locator, attribute):
    """
    :param self:
    :param locator: 元素定位器
    :param attribute: 元素属性
    :return: 返回元素属性值
    """
    return self.get_element_by_dict(locator).get_attribute(attribute)


# 输入文本
def send_keys(self, locator, text):
    """
    :param self:
    :param locator: 元素定位器
    :param text: 输入文本
    :return: None
    """
    self.get_element_by_dict(locator).send_keys(text)


# 清空文本
def clear_text(self, locator):
    """
    :param self:
    :param locator: 元素定位器
    :return: None
    """
    self.get_element_by_dict(locator).clear()


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
def get_element_location(self, locator):
    """
    :param self:
    :param locator: 元素定位器
    :return: 返回元素坐标
    """
    return self.get_element_by_dict(locator).location


# 拖动元素到指定位置
def drag_element(self, locator, x, y):
    """
    :param self:
    :param locator: 元素定位器
    :param x: x轴偏移量
    :param y: y轴偏移量
    :return: None
    """
    self.driver.drag_and_drop(self.get_element_by_dict(locator), x, y)


# 拖动元素到指定元素
def drag_element_to_element(self, locator1, locator2):
    """
    :param self:
    :param locator1: 元素1定位器
    :param locator2: 元素2定位器
    :return: None
    """
    self.driver.drag_and_drop(self.get_element_by_dict(locator1), self.get_element_by_dict(locator2))
