from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    """
    tv_agree: 提醒弹窗的知道
    iv_close: 登录弹窗的取消
    tips: 假数据

    _black_list: 黑名单（关闭弹窗的元素）
    """
    _black_list = [(By.ID, 'tv_agree'),
                   (By.ID, 'tips'),
                   (By.ID, 'iv_close')]

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        print(locator)
        # noinspection PyBroadException
        try:
            return self.driver.find_element(*locator)
        except:
            self.handle_exception()
            return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        print('click')
        self.find_element(locator).click()

    def handle_exception(self):
        print('exception')
        self.driver.implicitly_wait(1)
        for locator in self._black_list:
            # 通过寻找元素的方法去定位分析处理，性能相对差一点
            elements = self.driver.find_elements(*locator)
            if len(elements) >= 1:
                elements[0].click()
            else:
                print('%s not found' % locator[-1])

            # # 通过页面源代码去定位分析处理，性能相对好一点
            # page_source = self.driver.page_source
            # if locator[-1] in page_source:
            #     self.driver.find_element(*locator).click()
            # elif 'tips' in page_source:
            #     pass

        self.driver.implicitly_wait(6)

