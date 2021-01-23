from features.pages.mobile.base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from features.objects.android.home_page_objects import HomePageObjects as aobj
from features.objects.ios.home_page_objects import HomePageObjects as iobj


class HomePage(BasePage):

	app_title = None
	accessibility_button = None
	app_frame = None

	def __init__(self, context):
		BasePage.__init__(self, context.driver)
		platform = BasePage.platform_name(context)

		if platform == "Android":
			self.objects = aobj()
		elif platform == "iOS":
			self.objects = iobj()
		else:
			self.objects = aobj()

	def check_if_frame_is_displayed(self, context):
		app_frame = context.driver.find_element(By.XPATH, self.objects.app_frame['xpath'])
		wait = WebDriverWait(self, 10)
		wait.until(EC.visibility_of(app_frame))

	def app_title_is_displayed(self, context):
		global app_title
		app_title = context.driver.find_element(By.XPATH, self.objects.app_title['xpath'])
		wait = WebDriverWait(self, 10)
		wait.until(EC.visibility_of(app_title))

	def get_app_title(self):
		return app_title.text

	def accessibility_button_is_displayed(self, context):
		global accessibility_button
		accessibility_button = context.driver.find_element(By.XPATH, self.objects.accessibility_button['xpath'])
		wait = WebDriverWait(self, 10)
		wait.until(EC.visibility_of(accessibility_button))

	def tap_accessibility(self):
		actions = TouchAction(self.driver)
		actions.tap(accessibility_button)
		actions.perform()


