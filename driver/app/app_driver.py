# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver import webelement, WebElement
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conf.setting import root_path
from utils.logging_tool.log_control import WARNING, ERROR
from utils.testdatas_tool.get_excel import json_cl_list
from utils.time_tool.time_control import get_now_time_format


class AppDriver:
    """
    二次封装appium里driver and element
    """

    def __init__(self, driver: webdriver) -> None:
        """
        初始化
        :param driver:
        """
        self.driver = driver
        pass

    def get_find_element(self, by_list: list) -> WebElement:
        """
        通过list确定定位方式和定位值并返回元素
        :param by_list:
        :return:
        """

        # 判断by_list[0]为那种定位方式
        if by_list[0] == "id":
            # 捕获NoSuchElementException异常
            try:
                element = self.driver.find_element(By.ID, by_list[1])
            except NoSuchElementException as e:
                ERROR.logger.error("元素定位失败，定位方式：" + by_list[0] + "，定位值：" + by_list[1])
                raise
        elif by_list[0] == "xpath":
            try:
                element = self.driver.find_element(By.XPATH, by_list[1])
            except NoSuchElementException as e:
                ERROR.logger.error("元素定位失败，定位方式：" + by_list[0] + "，定位值：" + by_list[1])
                raise
        elif by_list[0] == "class":
            try:
                element = self.driver.find_element(By.CLASS_NAME, by_list[1])
            except NoSuchElementException as e:
                ERROR.logger.error("元素定位失败，定位方式：" + by_list[0] + "，定位值：" + by_list[1])
                raise
        elif by_list[0] == "name":
            try:
                element = self.driver.find_element(By.NAME, by_list[1])
            except NoSuchElementException as e:
                ERROR.logger.error("元素定位失败，定位方式：" + by_list[0] + "，定位值：" + by_list[1])
                raise
        elif by_list[0] == "tag_name":
            try:
                element = self.driver.find_element(By.TAG_NAME, by_list[1])
            except NoSuchElementException as e:
                ERROR.logger.error("元素定位失败，定位方式：" + by_list[0] + "，定位值：" + by_list[1])
                raise
        elif by_list[0] == "link_text":
            try:
                element = self.driver.find_element(By.LINK_TEXT, by_list[1])
            except NoSuchElementException as e:
                ERROR.logger.error("元素定位失败，定位方式：" + by_list[0] + "，定位值：" + by_list[1])
                raise
        elif by_list[0] == "partial_link_text":
            try:
                element = self.driver.find_element(By.PARTIAL_LINK_TEXT, by_list[1])
            except NoSuchElementException as e:
                ERROR.logger.error("元素定位失败，定位方式：" + by_list[0] + "，定位值：" + by_list[1])
                raise
        elif by_list[0] == "css_selector":
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, by_list[1])
            except NoSuchElementException as e:
                ERROR.logger.error("元素定位失败，定位方式：" + by_list[0] + "，定位值：" + by_list[1])
                raise
        elif by_list[0] == "android_uiautomator":
            element = self.driver.find_element(By.ANDROID_UIAUTOMATOR, by_list[1])
        elif by_list[0] == "ios_uiautomation":
            element = self.driver.find_element(By.IOS_UIAUTOMATION, by_list[1])
        elif by_list[0] == "accessibility_id":
            element = self.driver.find_element(By.ACCESSIBILITY_ID, by_list[1])
        else:
            raise Exception("定位方式参数错误；" + by_list[0])

        if element is None:
            raise Exception("元素定位失败")
        return element

    # 判断元素是否存在
    def is_element_exist(self, by_list) -> bool:
        """
        判断元素是否存在
        :param by_list:
        :return:
        """
        try:
            self.get_find_element(by_list)
            return True
        except:
            return False

    def wait_element(self, element: webelement, time) -> None:
        """
        显示等待元素可见可操作
        :param element:
        :param time:
        :return:
        """
        WebDriverWait(self.driver, time).until(element.is_displayed() and element.is_enabled())
        pass

    # 上下左右滑动屏幕
    def swipe_screen(self, direction) -> None:
        """
        上下左右滑动屏幕
        :param direction:   up/down/left/right
        :return:
        """
        # 获取屏幕宽高
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        # 上滑
        if direction == "up":
            self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4)
        # 下滑
        elif direction == "down":
            self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4)
        # 左滑
        elif direction == "left":
            self.driver.swipe(width * 3 / 4, height / 2, width / 4, height / 2)
        # 右滑
        elif direction == "right":
            self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2)
        else:
            raise Exception("滑动方向错误")
        pass

    def drag_element(self, element: webelement, x, y) -> None:
        """
        拖动元素到指定位置
        :param element:
        :param x:
        :param y:
        :return:
        """
        self.driver.drag_and_drop_by_offset(element, x, y)
        pass

    def drag_element_to_element(self, element1: webelement, element2: webelement) -> None:
        """
        拖动元素到指定元素
        :param element1:
        :param element2:
        :return:
        """
        self.driver.drag_and_drop(element1, element2)
        pass

    def get_screenshot(self, path) -> None:
        """
        截取屏幕并保存
        :param path:
        :return:
        """
        # 获取screenshot文件夹相对路径
        screenshot_path = root_path() + "/files/screenshot/"
        # 当前时间
        time = get_now_time_format()
        # 截屏并拼接时间保存到screenshot文件夹下抛出异常
        try:
            self.driver.get_screenshot_as_file(screenshot_path + time + path)
        except Exception as e:
            WARNING.logger.warning("截图失败，原因：{}".format(e))
            pass

    def click_element(self, by_datas, by_key) -> None:
        """
        点击元素
        :param by_key:
        :param by_datas:
        :return:
        """
        list1 = json_cl_list(by_datas, by_key)
        self.get_find_element(list1).click()
        pass

    def click_element_ignore(self, by_datas, by_key) -> None:
        """
        忽略点击元素
        :param by_key:
        :param by_datas:
        :return:
        """
        list1 = json_cl_list(by_datas, by_key)
        try:
            self.get_find_element(list1).click()
        except Exception as e:
            WARNING.logger.warning("点击元素失败，原因：{}".format(e))
            pass

    # 输入内容
    def send_keys(self, by_datas, by_key, text) -> None:
        """
        先清空再输入
        :param by_key:
        :param by_datas:
        :param text:
        :return:
        """
        list1 = json_cl_list(by_datas, by_key)
        self.get_find_element(list1).clear()
        self.get_find_element(list1).send_keys(text)
        pass

    # 获取元素文本
    def get_text(self, by_datas, by_key) -> str:
        """
        获取元素文本
        :param by_key:
        :param by_datas:
        :return:
        """
        list1 = json_cl_list(by_datas, by_key)
        return self.get_find_element(list1).text

    # 获取toast文本
    def get_toast_text(self, text) -> str:
        """
        获取toast文本
        :param text:
        :return:
        """
        return self.driver.find_element_by_xpath(
            ".//*[contains(@text,'{}')]".format(text)).text



    # 结束appium会话
    def quit(self) -> None:
        """
        结束appium会话
        :return:
        """
        self.driver.quit()

    # 返回
    def back(self) -> None:
        """
        返回
        :return:
        """
        self.driver.back()
        pass

    # 强制等待
    def sleep_time(self, time) -> None:
        """
        强制等待
        :param time:
        :return:
        """
        time.sleep(time)
        pass
