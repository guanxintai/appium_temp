from appium import webdriver


class TestWeb:

    def setup(self):
        caps = {'browserName': 'chrome',
                'platformName': 'android',
                'deviceName': 'attention',
                'chromedriverExecutable': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'}

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def test_web_search(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('index-kw').send_keys('uzi')

    def teardown(self):
        pass

