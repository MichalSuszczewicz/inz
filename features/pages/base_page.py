from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback
import time


class BasePage(object):
    def __init__(self, browser, base_url='https://wi.zut.edu.pl'):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 30

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def visit(self, url):
        self.browser.get(url)

    # def __getattr__(self, what):
    #     try:
    #         if what in self.locator_dictionary.keys():
    #             try:
    #                 element = WebDriverWait(self.browser, self.timeout).until(
    #                     EC.presence_of_element_located(self.locator_dictionary[what])
    #                 )
    #             except(TimeoutException, StaleElementReferenceException):
    #                 traceback.print_exc()
    #
    #             try:
    #                 element = WebDriverWait(self.browser, self.timeout).until(
    #                     EC.visibility_of_element_located(self.locator_dictionary[what])
    #                 )
    #             except(TimeoutException, StaleElementReferenceException):
    #                 traceback.print_exc()
    #
    #             return self.find_element(*self.locator_dictionary[what])
    #     except AttributeError:
    #         super(BasePage, self).__getattribute__("method_missing")(what)
    #
    # def method_missing(self, what):
    #     print("No %s here!"%what)