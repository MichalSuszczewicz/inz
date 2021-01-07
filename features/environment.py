from selenium import webdriver as webd
from appium import webdriver
from behave import fixture
from behave import use_fixture
import os
from datetime import datetime



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
		print("===>Browser starts")
	elif profile == 'firefox':
		context.driver = webd.Firefox()
		print("===>Browser starts")
	else:
		context.driver = webd.Chrome()
		print("===>Browser starts")

	context.driver.maximize_window()
	context.driver.implicitly_wait(10)
	yield context.driver
	context.driver.quit()
	print("Scenario time duration in seconds: ", context.scenario.duration)
	print("===>Browser is quit")


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
		print("===>App starts")

	elif profile == 'ios':
		dc['app'] = ''
		dc['platformName'] = 'iOS'
		dc['platformVersion'] = ''
		dc['deviceName'] = ''
		dc['automationName'] = 'XCUITest'
		dc["newCommandTimeout"] = 300
		context.driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
		print("===>App is quit")
	else:
		print('Precise your profile, use android or ios')

	yield context.driver
	context.driver.quit()
	print("Scenario time duration in seconds: ", context.scenario.duration)
	print("===>App starts")


def before_scenario(context, scenario):

	if 'profile' in context.config.userdata.keys():
		if context.config.userdata['profile'] is None:
			profile = 'chrome'
		else:
			profile = context.config.userdata['profile']
	else:
		profile = 'chrome'

	if profile == 'android' or profile == 'ios':

		use_fixture(mobile, context)

	elif profile == 'chrome' or profile == 'firefox':
		use_fixture(web, context)


def after_step(context, step):
	if step.status == 'failed':
		now = datetime.now()
		context.driver.save_screenshot(os.getcwd()+"/screenshots/"+step.name+now.strftime("%m_%d_%Y_%H_%M_%S")+".png")
