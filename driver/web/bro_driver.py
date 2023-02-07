"""
二次封装selenium的窗口操作方法
"""
from selenium import webdriver

from conf.setting import root_path
from utils.logging_tool.log_control import WARNING
from utils.time_tool.time_control import get_now_time_format


class BroDriver:

    # 初始化
    def __init__(self, driver: webdriver):
        self.driver = driver

    # 打开一个网址并判断网址格式是否正确
    def open_url(self, url):
        """
        :param url: 网址
        :return: None
        """
        if url.startswith("http") or url.startswith("https"):
            self.driver.get(url)
        else:
            raise Exception("网址格式错误")

    # 获取当前窗口url
    def get_current_url(self):
        return self.driver.current_url

    # 切换至新窗口
    def switch_to_new_window(self):
        """
        :return: None
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])

    # 窗口最大化
    def max_window(self):
        self.driver.maximize_window()

    # 隐式等待5秒
    def wait(self, s: int):
        self.driver.implicitly_wait(s)

    # 显示等待元素可见可点击否则抛出异常
    def wait_element_clickable(self, locator, s: int):
        """
        :param locator: 元素定位器
        :param s: 等待时间
        :return: 返回元素
        """
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        return WebDriverWait(self.driver, s).until(EC.element_to_be_clickable(locator))

    # 获取浏览器所有窗口句柄与url绑定，并根据url切换窗口
    def switch_window_by_url(self, url):
        """
        :param url: 窗口url
        :return: None
        """
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.current_url == url:
                break

    # 关闭浏览器
    def close_browser(self):
        self.driver.quit()

    # 打印弹窗信息并且通过布尔值判断是否关闭弹窗
    def alert(self, is_close: bool):
        """
        :param is_close: 布尔值
        :return: None
        """
        alert = self.driver.switch_to.alert
        print(alert.text)
        if is_close:
            alert.accept()
        else:
            alert.dismiss()

    # 定义一个截屏方法
    def screenshot(self):
        # 获取screenshot文件夹相对路径
        screenshot_path = root_path()+"/files/screenshot/"
        # 获取该页面标题
        title = self.driver.title
        # 当前时间
        time = get_now_time_format()
        # 截屏并拼接title和time保存到screenshot文件夹下抛出异常
        try:
            self.driver.get_screenshot_as_file(screenshot_path+"_"+title+"_"+time+".png")
        except Exception as e:
            WARNING.logger.warning("截图失败，原因：{}".format(e))

    # 清空cookies
    def clear_cookies(self):
        self.driver.delete_all_cookies()
