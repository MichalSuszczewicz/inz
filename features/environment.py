from selenium import webdriver
from features.pages.base_page import BasePage


def before_scenario(context, scenario):
    if 'browser' in context.config.userdata.keys():
        if context.config.userdata['browser'] is None:
            browser = 'chrome'
        else:
            browser = context.config.userdata['browser']
    else:
        browser = 'chrome'

    if browser == 'chrome':
        context.browser = webdriver.Chrome()
    elif browser == 'firefox':
        context.browser = webdriver.Firefox()
    # elif browser == 'opera':
    #     context.browser = webdriver.Opera()
    else:
        context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.implicitly_wait(10)


def after_scenario(context, scenario):
    context.browser.quit()
