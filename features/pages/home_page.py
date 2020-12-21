from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class HomePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self,context.browser, base_url='https://wi.zut.edu.pl')

        self.home_page_title = 'body > div:nth-child(5) > div > div.col-sm-6.wi-header > a > span'

    def locate_element(self):
        self.find_element(By.CSS_SELECTOR, self.home_page_title)


    def read_element(self):
        self.find_element(By.CSS_SELECTOR, 'body > div:nth-child(5) > div > div.col-sm-6.wi-header > a > span').getText()
