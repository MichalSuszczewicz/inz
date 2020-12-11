from pages.base_page import BasePage


class HomePage(BasePage):
    def locate_element(self):
        self._driver.find_element_by_css_selector('body > div:nth-child(5) > div > div.col-sm-6.wi-header > a > span')

    def read_element(self):
        return self._driver.find_element_by_css_selector('body > div:nth-child(5) > div > div.col-sm-6.wi-header > a > span').text
