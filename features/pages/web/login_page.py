from features.pages.web.base_page import BasePage
from features.objects.web.login_page_objects import *


class LoginPage(BasePage):

	log_in_button = None
	login_input = None
	password_input = None
	error_field = None
	error = None

	def __init__(self, context):
		BasePage.__init__(self, context.driver, base_url='https://wi.zut.edu.pl')
		self.objects = LoginPageObjects()

	def check_if_login_form_is_displayed(self, context):
		login_form = context.driver.find_element_by_xpath(self.objects.login_form['xpath'])

		login_form.is_displayed()

	def check_if_login_inputs_are_displayed(self, context):
		global login_input, password_input

		password_input = context.driver.find_element_by_xpath(self.objects.password_input['xpath'])
		login_input = context.driver.find_element_by_xpath(self.objects.login_input['xpath'])

		login_input.is_displayed()
		password_input.is_displayed()

	def check_if_log_in_button_is_displayed(self, context):
		global log_in_button

		log_in_button = context.driver.find_element_by_xpath(self.objects.log_in_button['xpath'])

		log_in_button.is_displayed()

	def get_button_text(self):
		return log_in_button.text

	def send_text_to_login_input(self, text):
		login_input.send_keys(text)

	def send_text_to_password_input(self, text):
		password_input.send_keys(text)

	def click_log_in_button(self):
		log_in_button.click()

	def check_if_error_message_displayed(self, context):
		global error, error_field
		error_field = context.driver.find_element_by_xpath(self.objects.error_field['xpath'])
		error = context.driver.find_element_by_xpath(self.objects.error['xpath'])
		error_field.is_displayed()
		error.is_displayed()

	def get_error_message(self):
		return error.text
