from features.pages.mobile.base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from features.objects.android.home_page_objects import *


class HomePage(BasePage):

	def __init__(self, context):
		BasePage.__init__(self,context.driver)
		objects = HomePageObjects()


		self.app_title = context.driver.find_element(By.XPATH,objects.app_title['xpath'])
		self.accessibility_button = context.driver.find_element(By.XPATH,objects.accessibility_button['xpath'])
		self.app_frame = context.driver.find_element(By.XPATH,objects.app_frame['xpath'])

	def check_if_frame_is_displayed(self):
		wait = WebDriverWait(self, 10)
		wait.until(EC.visibility_of(self.app_frame))

	def app_title_is_displayed(self):
		wait = WebDriverWait(self, 10)
		wait.until(EC.visibility_of(self.app_title))

	def get_app_title(self):
		return self.app_title.text

	def accessibility_button_is_displayed(self):
		wait = WebDriverWait(self, 10)
		wait.until(EC.visibility_of(self.accessibility_button))

	def tap_accessibility(self):
		actions = TouchAction(self.driver)
		actions.tap(self.accessibility_button)
		actions.perform()