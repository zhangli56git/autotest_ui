import time

from driver.driver_element import *
from page_object.base_page import BasePage
from utils.logging_tool.log_control import INFO
from utils.testdatas_tool.set_datas import list_bys


class LoginStep(BasePage):
    """
    fizz登录步骤页，加载固定页面by
    """

    def __init__(self, login_page_driver, login_page_bys):
        super().__init__(login_page_driver, login_page_bys)

    def page_ele(self, by_name) -> WebElement:
        pass

    def page_info(self):
        try:
            # 当前页面 url
            page_url = self.page_driver.get_url()
            # 当前页面 title
            page_title = self.page_driver.get_title()
            INFO.logger.info("当前页面url:{},页面title:{}".format(page_url, page_title))
        except Exception as e:
            INFO.logger.error("获取页面信息失败,可能为app".format())
        INFO.logger.info("当前页面元素信息:{}".format(self.page_bys))
        pass


    def is_upgrade(self):
        """
        判断是否升级
        :return:
        """
        click_element_ignore(self.page_ele("提示升级"))

    def is_home_page(self):
        """
        判断是否是首页
        :return:
        """
        # 判断底部我的元素是否显示
        ele = self.page_ele("底部我的").is_displayed()
        if not ele:
            with not ele:
                self.page_driver.back()
                ele = self.page_ele("底部我的").is_displayed()
        else:
            click_element(self.page_ele("底部我的"))

    def login_phone(self, phone, code) -> str:
        """
        手机号登录
        :param phone:   手机号
        :param code:    验证码
        :return:    None
        """
        click_element(self.page_ele("点击登录"))
        ele = self.page_ele("点击协议")
        if not ele.is_selected():
            click_element(ele)
        click_element(self.page_ele("手机登录"))
        click_element(self.page_ele("点击区号"))
        click_element(self.page_ele("选择地区"))
        input_element(self.page_ele("输入号码"), True, phone)
        click_element(self.page_ele("获取验证"))
        input_element(self.page_ele("输入验证"), True, code)
        click_element(self.page_ele("提交登录"))
        actual_text = "登录成功"
        try:
            self.page_driver.get_alert_text()
            actual_text = "登录失败"
        except Exception as e:
            INFO.logger.info("未找到错误登录提示toast")
        return actual_text

    # 首页签到
    def sign_in(self):
        """
        首页签到
        :return:
        """
        click_element_ignore(self.page_ele("首页签到"))

