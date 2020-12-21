from selenium import webdriver
from features.pages.base_page import BasePage


def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.implicitly_wait(10)


def after_scenario(context, scenario):
    context.browser.quit()
