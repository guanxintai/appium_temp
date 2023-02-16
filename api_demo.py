from appium import webdriver


class TestApiDemo:
    def setup(self):
        caps = {'platformName': 'android',
                'deviceName': 'attention',
                'appPackage': 'io.appium.android.apis',
                'appActivity': '.ApiDemos',
                'unicodeKeyboard': True,
                'autoGrantPermissions': True}

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def test_toast(self):
        self.driver.find_element_by_accessibility_id('Views').click()
        # 滑动操作，自动化定位到文本内容中
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Popup Menu").instance(0))'
        ).click()
        self.driver.find_element_by_accessibility_id('Make a Popup!').click()
        assert len(self.driver.find_elements_by_xpath('//*[@text="Edit"]')) == 1
        self.driver.find_element_by_xpath('//*[@text="Search"]').click()
        assert('Clicked popup menu item Search' in self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text)

    def teardown(self):
        pass
        # self.driver.quit()
