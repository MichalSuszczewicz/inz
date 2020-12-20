from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import *


class HomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self,context.browser, base_url='https://wi.zut.edu.pl')
        #self.context = context

    def locate_element(self):
        self.find_element(By.CSS_SELECTOR, 'body > div:nth-child(5) > div > div.col-sm-6.wi-header > a > span')


    def read_element(self):
        self.find_element(By.CSS_SELECTOR, 'body > div:nth-child(5) > div > div.col-sm-6.wi-header > a > span').getText()
