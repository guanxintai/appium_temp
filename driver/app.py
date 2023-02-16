import os
from appium import webdriver
from selenium.webdriver.common import utils
from selenium.webdriver.remote.webdriver import WebDriver
from page.main_page import MainPage


class App(object):
    driver: WebDriver

    @classmethod
    def start(cls):
        caps = {'platformName': 'android',
                'deviceName': 'attention',
                'appPackage': 'com.xueqiu.android',
                'appActivity': '.view.WelcomeActivityAlias',
                'chromedriverExecutable': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
                'unicodeKeyboard': True,
                'autoGrantPermissions': True,
                'udid': os.getenv('udid', None),
                'systemPort': utils.free_port(),
                'chromedriverPort': utils.free_port()}

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        cls.driver.implicitly_wait(20)

        # WebDriverWait === 显示等待，通过查找元素的方式 until是判断方法返回true or false
        # WebDriverWait(self.driver, 15).until(
        #     expected_conditions.visibility_of_element_located((By.ID, 'tv_agree'))
        # )
        # cls.driver.find_element_by_id('tv_agree').click()
        # def loaded():
        #     print(datetime.datetime.now())
        #     if len(self.driver.find_elements_by_id('tv_agree')) >= 1:
        #         self.driver.find_element_by_id('tv_agree').click()
        #         return True
        #     else:
        #         return False
        #
        # # noinspection PyBroadException
        # try:
        #     WebDriverWait(self.driver, 15).until(loaded)
        #     print('*' * 20)
        # except:
        #     print('no notices')
        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()
