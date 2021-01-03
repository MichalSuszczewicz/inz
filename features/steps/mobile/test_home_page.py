from features.pages.mobile.home_page import HomePage
from behave import *
from selenium import webdriver


@given('App is opened')
def test_case_name(context):
    home_page = HomePage(context)
    #home_page.check_if_frame_is_displayed()



@then('I see app title "{app_title}"')
def test_case_name(context, app_title):
    home_page = HomePage(context)
    #home_page.app_title.is_displayed()
    assert home_page.app_title.text == app_title


@step('I can navigate through the app')
def test_case_name(context):
    home_page = HomePage(context)
    home_page.tap_accessibility()
    #home_page.accessibility_button.is_displayed()
    #home_page.accessibility_button.tap()

