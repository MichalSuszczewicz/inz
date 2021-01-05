from features.pages.web.base_page import BasePage

from selenium.webdriver.common.by import By


class HomePage(BasePage):

	def __init__(self, context):
		BasePage.__init__(self,context.driver, base_url='https://wi.zut.edu.pl')

		self.home_page_title = context.driver.find_element_by_css_selector('body > div:nth-child(5) > div > div.col-sm-6.wi-header > a > span')

	def check_if_title_is_displayed(self):
		self.home_page_title.is_displayed()

	def get_page_title(self):
		return self.home_page_title.text
	#
	# def read_element(self):
	# 	print(self.home_page_title.text)
	# 	return self.home_page_title.text
