from selenium import webdriver as webd
from appium import webdriver
from behave import fixture
from behave import use_fixture
import os


@fixture
def web(context):
	if 'profile' in context.config.userdata.keys():
		if context.config.userdata['profile'] is None:
			profile = 'chrome'
		else:
			profile = context.config.userdata['profile']
	else:
		profile = 'chrome'

	if profile == 'chrome':
		context.driver = webd.Chrome()
	elif profile == 'firefox':
		context.driver = webd.Firefox()
	else:
		context.driver = webd.Chrome()

	context.driver.maximize_window()
	context.driver.implicitly_wait(10)
	yield context.driver
	context.driver.quit()

@fixture
def mobile(context):
	dc = {}



	if 'profile' in context.config.userdata.keys():
		if context.config.userdata['profile'] is None:
			profile = 'android'
		else:
			profile = context.config.userdata['profile']
	else:
		profile = 'android'

	if profile == 'android':

		dc['app'] = os.getcwd()+'/app/ApiDemos-debug.apk'
		dc['platformName'] = 'Android'
		dc['deviceName'] = 'Pixel 3 API 29'
		dc['automationName'] = 'UiAutomator2'
		dc["newCommandTimeout"] = 300

		context.driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)

	elif profile == 'ios':
		dc['app'] = ''
		dc['platformName'] = 'iOS'
		dc['platformVersion'] = ''
		dc['deviceName'] = ''
		dc['automationName'] = 'XCUITest'
		dc["newCommandTimeout"] = 300
		context.driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
	else:
		print('Precise your profile, use android or ios')

	yield context.driver
	context.driver.quit()


def before_tag(context, tag):
	if tag == 'fixture.web':
		use_fixture(web, context)
	elif tag == 'fixture.mobile':
		use_fixture(mobile, context)