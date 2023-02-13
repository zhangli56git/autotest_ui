import time

from page_object.pages.base_page import BasePage
from utils.logging_tool.log_control import INFO
from utils.testdatas_tool.get_excel import GetExcel, excel_cell_list


class LoginStep(BasePage):
    """
    fizz登录步骤页，加载固定页面by
    """

    # 初始化
    def __init__(self, driver, by_page_datas):
        super().__init__(driver)
        self.by_page_datas = by_page_datas
        INFO.logger.info("\n" + self.by_page_datas)

    # 是否升级
    def is_upgrade(self):
        by_upgrade = excel_cell_list(self.by_page_datas, "提示升级")
        if self.driver.is_element_exist(by_upgrade):
            self.driver.click_element(self.by_page_datas, "提示升级")
        else:
            print("无升级提示")

    # 确定在登录页
    def is_login_page(self):
        by_bottom = excel_cell_list(self.by_page_datas, "底部我的")
        # 定义一个布尔值
        is_bottom = self.driver.is_element_exist(by_bottom)
        # 如果is_bottom未假时执行
        if not is_bottom:
            # 循环 is_bottom为假时执行
            while not is_bottom:
                self.driver.back()
                is_bottom = self.driver.is_element_exist(by_bottom)
        else:
            self.driver.click_element(self.by_page_datas, "底部我的")

    # 手机号登录
    def login_phone_step(self, phone, code) -> str:
        self.driver.click_element(self.by_page_datas, "点击登录")
        element = self.driver.get_find_element(excel_cell_list(self.by_page_datas, "点击协议"))
        if not element.is_selected():
            self.driver.click_element(self.by_page_datas, "点击协议")
        self.driver.click_element(self.by_page_datas, "手机登录")
        self.driver.click_element(self.by_page_datas, "点击区号")
        self.driver.click_element(self.by_page_datas, "选择地区")
        self.driver.send_keys(self.by_page_datas, "输入号码", phone)
        self.driver.click_element(self.by_page_datas, "获取验证")
        self.driver.send_keys(self.by_page_datas, "输入验证", code)
        self.driver.click_element(self.by_page_datas, "提交登录")
        # 获取提示文本
        try:
            self.driver.get_toast_text("登录是否")
            actual_text = "登录失败"
        except Exception as e:
            INFO.logger.info("未找到登录提示toast")
            actual_text = "登录成功"
        return actual_text

    # 首页签到按钮
    def sign_in(self):
        if self.driver.is_element_exist(excel_cell_list(self.by_page_datas, "首页签到")):
            self.driver.click_element(self.by_page_datas, "首页签到")
        else:
            INFO.logger.info("未找到签到按钮")
