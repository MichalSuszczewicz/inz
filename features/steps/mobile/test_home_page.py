from features.pages.mobile.home_page import HomePage
from behave import *

@given('App is opened')
def test_case_name(context):
    home_page = HomePage(context)
    home_page.check_if_frame_is_displayed(context)



@then('I see app title "{title}"')
def test_case_name(context, title):
    home_page = HomePage(context)
    home_page.app_title_is_displayed(context)
    assert home_page.get_app_title() == title


@step('I can navigate through the app')
def test_case_name(context):
    home_page = HomePage(context)
    home_page.accessibility_button_is_displayed(context)
    home_page.tap_accessibility()

