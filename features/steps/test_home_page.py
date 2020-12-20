from features.pages.home_page import HomePage
#from features.config import Template
from behave import given, when, then


#class TestHomePage(Template):

@given('I am on wi zut page')
def test_case_name(context):
    context.browser.get('https://wi.zut.edu.pl')
   # home_page = HomePage(context)
   # home_page.visit('https://wi.zut.edu.pl')
   # home_page.base_url = 'https://wi.zut.edu.pl'

@then('I see wi zut title')
def test_case_name(context):
    #return 1
    home_page = HomePage(context)
    home_page.locate_element()
    assert home_page.read_element() == "Wydział Informatyki"