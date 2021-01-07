from features.pages.mobile.home_page import HomePage
from behave import *

@given('App is opened')
def test_case_name(context):
    home_page = HomePage(context)
    home_page.check_if_frame_is_displayed()



@then('I see app title "{app_title}"')
def test_case_name(context, app_title):
    home_page = HomePage(context)
    home_page.app_title.is_displayed()
    assert home_page.get_app_title() == app_title


@step('I can navigate through the app')
def test_case_name(context):
    home_page = HomePage(context)
    home_page.accessibility_button_is_displayed()
    home_page.tap_accessibility()

