from features.pages.base_page import BasePage
from selenium import *


class HomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser, base_url = 'https://wi.zut.edu.pl')

    def locate_element(self):
        return 1

    def read_element(self):
        return 1
