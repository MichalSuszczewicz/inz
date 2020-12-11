from pages.home_page import HomePage
from config import Template
from radish import given, when, then


class TestHomePage(Template):

    @given("I am on wi zut page")
    def test_case_name(self):
        home_page = HomePage(self.driver)

    @then("I see wi zut title")
    def test_case(self):
        home_page = HomePage(self.driver)
        home_page.locate_element()
        assert home_page.read_element() == "Wydział Informatyki"