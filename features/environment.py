from selenium import webdriver
from features.pages.base_page import BasePage

def before_all(context):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    context.browser = BasePage(driver)
    context

#def after_scenario(context, scenario):
 #   context.browser.screenshot(str(scenario))
