from features.pages.web.login_page import LoginPage
from features.pages.web.home_page import HomePage
from behave import given, then, when


@when('uzytkownik kliknie przycisk logowania')
def test_case_name(context):
    home_page = HomePage(context)
    home_page.check_if_login_button_is_displayed_and_click_it(context)


@then('uzytkownik widzi strone logowania')
def test_case_name(context):
    login_page = LoginPage(context)
    login_page.check_if_login_form_is_displayed(context)
    login_page.check_if_login_inputs_are_displayed(context)


@when('uzytkownik wpisze login "{login}"')
def test_case_name(context, login):
    login_page = LoginPage(context)
    login_page.send_text_to_login_input(login)

@when('uzytkownik wpisze haslo "{password}"')
def test_case_name(context, password):
    login_page = LoginPage(context)
    login_page.send_text_to_password_input(password)

@when('uzytkownik kliknie przycisk "{button}"')
def test_case_name(context, button):
    login_page = LoginPage(context)
    login_page.check_if_log_in_button_is_displayed(context)
    assert login_page.get_button_text() == button
    login_page.click_log_in_button()

@then('zostaje wyswietlony komunikat o bledzie "{error}"')
def test_case_name(context, error):
    login_page = LoginPage(context)
    login_page.check_if_error_message_displayed(context)
    assert login_page.get_error_message() == error


