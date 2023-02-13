"""
创建一个class，用于二次封装selenium中的元素操作
"""
from selenium.common import exceptions
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conf.setting import root_path
from driver.driver_base import DriverBase
from utils.logging_tool.log_control import INFO, ERROR, WARNING
from utils.time_tool.time_control import get_now_time_format
from io import BytesIO
from PIL import Image

class ElementBase(DriverBase):
    """
    二次封装selenium中的元素操作
    """

    # 初始化
    def __init__(self, driver):
        super().__init__(driver)

    '''
        元素操作    ---------------------------------------------------
    '''

    # 根据元祖选择定位方式并返回元素
    def get_element(self, *locator) -> WebElement:
        """
        根据元祖选择定位方式并返回元素
        :param locator:     元祖类型    (定位名称,定位方式,定位值)
        :return:        元素
        """

        # 先判断locator不为空和长度为3
        if not locator and len(locator) != 3:
            ERROR.logger.error("locator传入错误=>{}".format(locator))
            raise TypeError()

        # 声明一个变量获取定位方式
        by_select = ['By.ID', 'By.XPATH', 'By.LINK_TEXT', 'By.PARTIAL_LINK_TEXT', 'By.NAME', 'By.TAG_NAME',
                     'By.CLASS_NAME', 'By.CSS_SELECTOR']

        # 获取元祖中的值
        by_type = locator[1]
        by_value = locator[2]

        # 判断定位方式是否正确
        if by_type not in by_select:
            ERROR.logger.error("locator方式传入错误=>{}".format(by_type))
            raise KeyError()
        else:
            INFO.logger.info("操作元素=>{}".format(locator))

        # 根据locator定位返回element
        try:
            element_value = self.driver.find_element(by_type, by_value)
        except exceptions.NoSuchElementException() as e:
            ERROR.logger.error("元素定位失败=>{}".format(locator))
            raise e
        return element_value

    def click_element(self, element_v: WebElement) -> None:
        """
        点击元素
        :param element_v:
        :return:
        """
        # 捕获点击异常
        try:
            element_v.click()
        except Exception as e:
            ERROR.logger.error("元素点击失败=>{}".format(element_v))
            raise e


    # 忽略点击
    def click_element_ignore(self, element_v: WebElement) -> None:
        """
        忽略点击
        :param element_v:
        :return:
        """
        try:
            element_v.click()
        except exceptions.ElementNotInteractableException:
            WARNING.logger.info("忽略该元素点击=>{}".format(element_v))
            pass

    def input_element(self, element_v: WebElement, clear: bool, text) -> None:
        """
        输入文本
        :param element_v:
        :param clear:
        :param text:
        :return:
        """
        if clear:
            element_v.clear()
        element_v.send_keys(text)

    def get_text(self, element_v: WebElement) -> str:
        """
        获取元素文本
        :param element_v:
        :return: 元素文本
        """
        return element_v.text

    def wait_for_element(self, element_v: WebElement, timeout=5):
        """
        显示等待元素
        :param element_v:
        :param timeout:
        :return:
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable(element_v))
            return element
        except:
            WARNING.logger.error("元素等待失败=>{}".format(element_v))
        return element

    # 拖动元素
    def drag_element(self, element_v: WebElement, x, y) -> None:
        """
        拖动元素
        :param element_v:
        :param x:
        :param y:
        :return:
        """
        ActionChains(self.driver).drag_and_drop_by_offset(element_v, x, y).perform()

    # 进入iframe
    def switch_to_iframe(self, element_v: WebElement) -> None:
        """
        进入iframe
        :param element_v:
        :return:
        """
        self.driver.switch_to.frame(element_v)

    # 退出iframe
    def switch_to_default_content(self) -> None:
        """
        退出iframe
        :return:
        """
        self.driver.switch_to.default_content()

    # 上下左右滑动屏幕
    def swipe_screen(self, direction, duration=1000) -> None:
        """
        上下左右滑动屏幕
        :param direction:   方向
        :param duration:    滑动时间
        :return:
        """
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        if direction == 'up':
            self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, duration)
        elif direction == 'down':
            self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, duration)
        elif direction == 'left':
            self.driver.swipe(width * 3 / 4, height / 2, width / 4, height / 2, duration)
        elif direction == 'right':
            self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, duration)
        else:
            ERROR.logger.error("direction参数错误=>{}".format(direction))
            raise ValueError()

        # 拖动元素到指定元素
    def drag_element_to_element(self, element_v: WebElement, element_v2: WebElement) -> None:
        """
        拖动元素到指定元素
        :param element_v:
        :param element_v2:
        :return:
        """
        ActionChains(self.driver).drag_and_drop(element_v, element_v2).perform()

    # 截取元素图片
    def get_element_screenshot(self, element_v: WebElement) -> None:
        """
        截取元素图片
        :param element_v:
        :return:
        """
        # 获取screenshot文件夹相对路径
        screenshot_path = root_path() + "/files/screenshot/"
        # 获取该页面标题
        title = self.driver.title
        # 当前时间
        time = get_now_time_format()
        # 截图文件名
        location = element_v.location
        size = element_v.size
        png = self.driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom))
        try:
            im.save(screenshot_path + title + "_" + time + ".png")
        except Exception as e:
            WARNING.logger.error("截图失败=>{}".format(e))


