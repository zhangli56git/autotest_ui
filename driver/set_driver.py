from driver.driver_element import DriverElement


class SetDriver(DriverElement):
    """
    用来继承的基类
    """

        # 初始化
    def __init__(self, driver_name):
        """
        :param driver_name:     driver名称
        """
        super().__init__(driver_name=driver_name)


if __name__ == '__main__':
    qwe = SetDriver(driver_name="chrome")
