from abc import ABCMeta, abstractmethod

from driver.app.app_driver import AppDriver


class BasePage(metaclass=ABCMeta):
    """
    BasePage封装所有页面都公用的方法，比如driver，url，FindElement等
    """

    def __init__(self, driver: AppDriver):
        """
        初始化driver
        :param driver:
        """
        self.driver = driver

    # @abstractmethod
    # def get_page_by_data(self, file_name, sheet_name) -> None:
    #     """
    #     获取页面所有by定位值
    #     :param file_name:
    #     :param sheet_name:
    #     :return:
    #     """
    #     pass
