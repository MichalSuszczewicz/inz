from features.pages.mobile.base_page import BasePage
from appium.webdriver.common.touch_action import TouchAction


class HomePage(BasePage):

	def __init__(self, context):
		BasePage.__init__(self,context.driver)

		self.app_title = context.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView')
		self.accessibility_button = context.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Accessibility"]')
		self.app_frame = context.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup')

	def check_if_frame_is_displayed(self):
		self.app_frame.visible()

	def tap_accessibility(self):
		# actions = TouchAction(self)
		# actions.tap(self.accessibility_button)
		# self.actions.perform()
		self.accessibility_button.click()