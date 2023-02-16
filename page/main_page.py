from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.search_page import SearchPage


class MainPage(BasePage):
    _search_locator = (By.ID, 'tv_search')

    def to_search(self):
        self.find_element_and_click(self._search_locator)
        return SearchPage(self.driver)

