"""
创建一个class，用于二次封装webdriver，实现一些常用的方法
"""
from selenium import webdriver
from conf.setting import root_path
from utils.logging_tool.log_control import WARNING, INFO
from utils.time_tool.time_control import get_now_time_format


class DriverBase:
    """
    二次封装webdriver
    """

    # 初始化
    def __init__(self, driver: webdriver):
        self.driver = driver

    '''
        driver操作    ---------------------------------------------------
    '''

    def get(self, url) -> None:
        """
        打开url
        :param url: url地址
        :return:    None
        """
        self.driver.get(url)

    def quit(self) -> None:
        """
        退出driver
        :return:    None
        """
        self.driver.quit()

    def close(self) -> None:
        """
        关闭driver
        :return:    None
        """
        self.driver.close()

    def back(self) -> None:
        """
        返回上一步
        :return:    None
        """
        self.driver.back()

    def forward(self) -> None:
        """
        前进
        :return:    None
        """
        self.driver.forward()

    def refresh(self) -> None:
        """
        刷新
        :return:    None
        """
        self.driver.refresh()

    def get_title(self) -> str:
        """
        获取title
        :return:    str
        """
        return self.driver.title

    def get_url(self) -> str:
        """
        获取url
        :return:    str
        """
        return self.driver.current_url

    def get_window_size(self) -> dict:
        """
        获取窗口大小
        :return:    dict
        """
        return self.driver.get_window_size()

    def set_window_max(self) -> None:
        """
        设置窗口最大化
        :return:    None
        """
        self.driver.maximize_window()

    def set_window_min(self) -> None:
        """
        设置窗口最小化
        :return:    None
        """
        self.driver.minimize_window()

    # 切换至新窗口
    def switch_to_new_window(self) -> None:
        """
        切换至新窗口
        :return:    None
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])

    # 获取所有窗口句柄并根据url且换窗口
    def switch_to_window_by_url(self, url) -> None:
        """
        获取所有窗口句柄并根据url且换窗口
        :param url: url地址
        :return:    None
        """
        # 获取所有窗口句柄
        handles = self.driver.window_handles
        # 遍历句柄，切换至对应url的窗口
        for handle in handles:
            self.driver.switch_to.window(handle)
            if self.driver.current_url == url:
                break

    # 获取提示框文本根据布尔参数确定是否点击'确定'按钮
    def get_alert_text(self, is_click: bool) -> str:
        """
        获取提示框文本根据布尔参数确定是否点击'确定'按钮
        :param is_click:
        :return:
        """
        alert = self.driver.switch_to.alert
        text = alert.text
        INFO.logger.info("提示框文本=>{}".format(text))
        if is_click:
            alert.accept()
        else:
            alert.dismiss()
        return text

    def screenshot(self) -> None:
        """
        截全屏图
        :return:    None
        """
        # 获取screenshot文件夹相对路径
        screenshot_path = root_path() + "/files/screenshot/"
        # 获取该页面标题
        title = self.driver.title
        # 当前时间
        time = get_now_time_format()
        # 截屏并拼接title和time保存到screenshot文件夹下抛出异常
        try:
            self.driver.get_screenshot_as_file(screenshot_path + "_" + title + "_" + time + ".png")
        except Exception as e:
            WARNING.logger.warning("截图失败，原因：{}".format(e))

    def clear_cookies(self) -> None:
        """
        清除cookies
        :return:
        """
        self.driver.delete_all_cookies()
