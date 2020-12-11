from pages.home_page import HomePage
from config import Template

class TestHomePage(Template):
    def test_case_name(self):
        home_page = HomePage(self.driver)
        home_page.locate_element()
        assert home_page.read_element() == "Wydział Informatyki"