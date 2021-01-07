from features.pages.web.home_page import HomePage
from behave import given, then

@given('I am on wi zut home page')
def test_case_name(context):
    context.driver.get('https://wi.zut.edu.pl')
    assert context.driver.current_url == 'https://www.wi.zut.edu.pl/pl/'



@then('I see wi zut title "{page_title}"')
def test_case_name(context, page_title):
    home_page = HomePage(context)
    home_page.check_if_title_is_displayed()
    assert home_page.get_page_title() == page_title

