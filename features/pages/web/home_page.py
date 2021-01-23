from features.pages.web.base_page import BasePage
from features.objects.web.home_page_objects import *


class HomePage(BasePage):

	home_page_title = None
	login_button = None

	def __init__(self, context):
		BasePage.__init__(self, context.driver, base_url='https://wi.zut.edu.pl')
		self.objects = HomePageObjects()

	def check_if_title_is_displayed(self, context):
		global home_page_title
		home_page_title = context.driver.find_element_by_css_selector(self.objects.page_title['css_selector'])
		home_page_title.is_displayed()

	def get_page_title(self):
		return home_page_title.text

	def check_if_login_button_is_displayed_and_click_it(self, context):
		global login_button
		login_button = context.driver.find_element_by_xpath(self.objects.login_button['xpath'])
		login_button.is_displayed()
		login_button.click()
