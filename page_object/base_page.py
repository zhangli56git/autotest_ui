# -*- coding: utf-8 -*-
import abc

from driver.set_driver import SetDriver
from utils.testdatas_tool.set_datas import list_bys


class BasePage(metaclass=abc.ABCMeta):
    """
    用来继承的基类
    """

    # 初始化
    def __init__(self, page_driver: SetDriver, page_bys):
        """
        :param page_driver:     driver
        :param page_bys:        bys
        """
        self.page_driver = page_driver
        self.page_bys = page_bys

    @abc.abstractmethod
    def page_ele(self, by_name):
        """
        获取页面元素
        :param by_name:
        :return:
        """
        return self.page_driver.get_element(list_bys(self.page_bys, by_name))
        pass

    @abc.abstractmethod
    def page_info(self):
        """
        输出页面基本信息
        :return:
        """
        pass
