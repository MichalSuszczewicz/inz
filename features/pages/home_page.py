from features.config import Template


class HomePage(Template):
    def locate_element(self):
        self.find_element_by_css_selector('body > div:nth-child(5) > div > div.col-sm-6.wi-header > a > span')

    def read_element(self):
        return self.find_element_by_css_selector('body > div:nth-child(5) > div > div.col-sm-6.wi-header > a > span').text
