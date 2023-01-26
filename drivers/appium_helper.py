
"""
创建一个appium_Helper的类用于二次封装appium里的方法
"""
class AppiumHelper:

    # 初始化方法
    def __init__(self, driver):
        self.driver = driver

    # 通过字典判断定位方式
    def get_element_by_dict(self, locator):
        """
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

    # 判断元素是否存在并打印到控制台
    def is_element_exist(self, locator):
        """
        :param locator: 元素定位器
        :return: 返回布尔值
        """
        try:
            self.get_element_by_dict(locator)
            print("元素存在")
            return True
        except Exception as e:
            print("元素不存在："+locator, e)
            return False

