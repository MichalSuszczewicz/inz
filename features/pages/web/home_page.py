from features.pages.web.base_page import BasePage
from features.objects.web.home_page_objects import *


class HomePage(BasePage):

	def __init__(self, context):
		BasePage.__init__(self,context.driver, base_url='https://wi.zut.edu.pl')
		objects = HomePageObjects()

		self.home_page_title = context.driver.find_element_by_css_selector(objects.page_title['css_selector'])

	def check_if_title_is_displayed(self):
		self.home_page_title.is_displayed()

	def get_page_title(self):
		return self.home_page_title.text
