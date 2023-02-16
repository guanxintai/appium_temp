from time import sleep
import pytest
import yaml
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions
from hamcrest import *
from page.search_page import SearchPage


class TestDemo:
    search_data = yaml.safe_load(open('data/search.yaml', 'r'))
    print(search_data)

    def setup(self):
        caps = {'platformName': 'android',
                'deviceName': 'attention',
                'appPackage': 'com.xueqiu.android',
                'appActivity': '.view.WelcomeActivityAlias',
                'chromedriverExecutable': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
                'unicodeKeyboard': True,
                'autoGrantPermissions': True,
                'udid': 'emulator-5554'}

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(20)

        # WebDriverWait === 显示等待，通过查找元素的方式 until是判断方法返回true or false
        # WebDriverWait(self.driver, 15).until(
        #     expected_conditions.((By.ID, 'tv_agree'))
        # )
        self.driver.find_element_by_id('tv_agree').click()
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

    def test_demo(self):
        # first case
        self.driver.find_element_by_id('tv_search').click()
        self.driver.find_element_by_id('search_input_text').send_keys('pdd')

    def test_capabilities(self):
        # 配置修改测试（输入中文）
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')

    def test_gsm_call(self):
        # 模拟打电话 发短信
        self.driver.make_gsm_call('15820474375', GsmCallActions.CALL)
        self.driver.send_sms('18159661442', '黑夜给了我黑色的眼睛，我却用它来寻找光明')

    def test_xpath(self):
        self.driver.find_element_by_xpath("//*[@text='行情']").click()

    @pytest.mark.parametrize('keyword, expected_price', search_data)
    def test_search_from_outer(self, keyword, expected_price):
        self.driver.find_element_by_id('tv_search').click()
        self.driver.find_element_by_id('search_input_text').send_keys(keyword)
        self.driver.find_element_by_id('name').click()
        price = self.driver.find_element_by_id('current_price')
        assert float(price.text) > expected_price
        assert_that(price.get_attribute('package'), equal_to('com.xueqiu.android'))

    @pytest.mark.parametrize('keyword, expected_price', [
        ('阿里巴巴', 200),
        ('拼多多', 100),
        ('腾讯', 500)
    ])
    def test_search(self, keyword, expected_price):
        self.driver.find_element_by_id('tv_search').click()
        self.driver.find_element_by_id('search_input_text').send_keys(keyword)
        self.driver.find_element_by_id('name').click()
        price = self.driver.find_element_by_id('current_price')
        assert float(price.text) > expected_price
        assert_that(price.get_attribute('package'), equal_to('com.xueqiu.android'))

    def test_webview(self):
        self.driver.find_element_by_xpath('//*[@text="交易"]').click()
        for i in range(5):
            print(self.driver.contexts)
        self.driver.find_element_by_xpath('//*[@text="A股开户"]').click()
        self.driver.switch_to.context(self.driver.contexts[-1])
        print(self.driver.current_context)
        self.driver.find_element_by_id('phone-number').send_keys('15820474375')

    def test_performance(self):
        print(self.driver.get_performance_data_types())
        for p in self.driver.get_performance_data_types():
            # noinspection PyBroadException
            try:
                print(self.driver.get_performance_data('com.xueqiu.android', p, 5))
            except:
                pass

    def test_search_po(self):
        search_page = SearchPage(self.driver)
        search_page.search('alibaba')
        assert search_page.get_current_price() > 10

    def teardown(self):
        # sleep(5)
        self.driver.quit()


