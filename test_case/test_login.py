import os

import allure
import pytest

from driver.app.app_conf import app_conf
from driver.app.app_driver import AppDriver
from page_object.modules.fizz_an_login_m import LoginMod
from utils.testdatas_tool.get_excel import GetExcelDatas

data_test = GetExcelDatas("template.xlsx", "login").get_excel_datas_calls("E2", "F2")


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
        driver_page_by = GetExcelDatas("template.xlsx", "login").get_excel_datas_call("by_element", 0)
        # 实例化登录模块保存by
        driver_page = LoginMod(driver_app, driver_page_by)
        # 获取该页by定位值
        driver_page.login_phone_mod(phone, code, expect)
        driver_app.quit()


if __name__ == '__main__':
    """
       --reruns: 失败重跑次数
       --count: 重复执行次数
       -v: 显示错误位置以及错误的详细信息
       -s: 等价于 pytest --capture=no 可以捕获print函数的输出
       -q: 简化输出信息
       -m: 运行指定标签的测试用例
       -x: 一旦错误，则停止运行
       --maxfail: 设置最大失败次数，当超出这个阈值时，则不会在执行测试用例
        "--reruns=3", "--reruns-delay=2"
    """

    # pytest.main(["-vs", "test_case/test_login.py", '--clean-alluredir', '--alluredir=reports/allurefile'])

    pytest.main(['-s', '-W', "test_case/test_login.py", 'ignore:Module already imported:pytest.PytestWarning',
                 '--alluredir', './report/tmp', "--clean-alluredir"])

    # os.system(r"allure generate ./report/tmp -o ./report/html --clean")
    # 程序运行之后，自动启动报告，如果不想启动报告，可注释这段代码
    # os.system(f"allure serve ./report/tmp -h 127.0.0.1 -p 49640")
