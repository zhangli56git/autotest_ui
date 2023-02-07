from page_object.pages.fizz_an_login_s import LoginStep
from utils.assertion.assert_type import assert_in, assert_equal


class LoginMod(LoginStep):

    # 初始化
    def __init__(self, driver, by_page_datas):
        super().__init__(driver, by_page_datas)

    # 登录模块
    def login_phone_mod(self, phone, code, expect_test):
        """
        登录模块并断言
        :param expect_test:
        :param phone:
        :param code:
        :return:
        """
        super().is_upgrade()
        super().is_login_page()
        actual_test = super().login_phone_step(phone, code)
        # assert_equal(actual=actual_test, expect=expect_test)
        super().sign_in()

