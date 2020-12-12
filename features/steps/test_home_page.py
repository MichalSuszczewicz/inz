from features.pages.home_page import HomePage
from features.config import Template
from behave import *


class TestHomePage(Template):

    @given('I am on wi zut page')
    def test_case_name(context):
        context.browser.get('https://wi.zut.edu.pl')

    @then('I see wi zut title')
    def test_case(context):
        home_page = HomePage(context)
        home_page.locate_element()
        assert home_page.read_element() == "Wydział Informatyki"