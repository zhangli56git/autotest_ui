from page_object.pages.fizz_an_login_s import LoginStep
from utils.assertion.assert_type import assert_in


class LoginMod:
    """
    登录模块
    """

    def __init__(self, login_page_driver, login_page_bys):
        self.login_step = LoginStep(login_page_driver, login_page_bys)

    def login_phone_mod(self, phone, code, expect_test):
        """
        手机登录模块
        :param phone:    手机号
        :param code:    验证码
        :param expect_test:     预期结果
        :return:
        """
        self.login_step.is_upgrade()
        self.login_step.is_home_page()
        actual_text = self.login_step.login_phone(phone, code)
        assert_in(actual=actual_text, expect=expect_test, msg="校验登录结果!!!")
        self.login_step.sign_in()

