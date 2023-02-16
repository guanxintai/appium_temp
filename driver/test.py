from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('action')
driver.find_element_by_id('su').click()

ActionChains(driver).drag_and_drop(source, target).perform()
