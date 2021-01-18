from features.pages.web.home_page import HomePage
from behave import given, then, when

@given('strona wi zut jest otwarta')
def test_case_name(context):
    assert context.driver.current_url == 'https://www.wi.zut.edu.pl/pl/'

@when('uzytkownik spojrzy na naglowek')
def test_case_name(context):
    home_page = HomePage(context)
    home_page.check_if_title_is_displayed(context)


@then('uzytkownik widzi tresc "{page_title}"')
def test_case_name(context, page_title):
    home_page = HomePage(context)
    assert home_page.get_page_title() == page_title

