import allure
import pytest

from driver.app_driver import app_conf
from driver.app.app_driver import AppDriver
from page_object.modules.fizz_an_login_m import LoginMod
from utils.testdatas_tool.get_excel import GetExcel

data_test = GetExcel("test_data.xlsx", "login").get_excel_datas_calls("E2", "F2")


@allure.epic("FIZZ安卓端UI自动化测试")
@allure.feature("登录模块")
class TestLoginFlow:

    @allure.story("登录")
    @pytest.mark.parametrize('phone, code, expect', [data_test])
    def test_login(self, phone, code, expect):
        """
        :param :
        :return:
        """
        # 启动app
        driver_app = AppDriver(app_conf("android"))
        # 获取页面参数
        driver_page_by = GetExcel("test_data.xlsx", "login").get_excel_datas_call("by_element", 0)
        # 实例化登录模块保存by
        driver_page = LoginMod(driver_app, driver_page_by)
        # 获取该页by定位值
        driver_page.login_phone_mod(phone, code, expect)
        driver_app.quit()


if __name__ == '__main__':



    pytest.main(['-s', '-W', "test_case/test_login.py", 'ignore:Module already imported:pytest.PytestWarning',
                 '--alluredir', './report/tmp', "--clean-alluredir"])

    # os.system(r"allure generate ./report/tmp -o ./report/html --clean")
    # 程序运行之后，自动启动报告，如果不想启动报告，可注释这段代码
    # os.system(f"allure serve ./report/tmp -h 127.0.0.1 -p 49640")
