from selenium import webdriver
from behave import fixture
from behave import use_fixture


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
		context.driver = webdriver.Chrome()
	elif profile == 'firefox':
		context.driver = webdriver.Firefox()
	else:
		context.driver = webdriver.Chrome()

	context.driver.maximize_window()
	context.driver.implicitly_wait(10)
	yield context.driver
	context.driver.quit()

@fixture
def mobile(context):
	dc = {}
	dc['app'] = '/Users/m.suszczewicz/Study/inz/inz/app/ApiDemos-debug.apk'
	dc['platformName'] = 'Android'
	dc['deviceName'] = 'Pixel 3 API 29'
	dc['automationName'] = 'UiAutomator2'
	dc["newCommandTimeout"] = 300

	if 'profile' in context.config.userdata.keys():
		if context.config.userdata['profile'] is None:
			profile = 'android'
		else:
			profile = context.config.userdata['profile']
	else:
		profile = 'android'

	if profile == 'android':
		context.driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
	elif profile == 'ios':
		context.driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
	else:
		context.driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)

	yield context.driver
	context.driver.quit()

# def before_scenario(context, scenario):
#
# 	dc = {}
# 	dc['app'] = '/Users/m.suszczewicz/Study/inz/inz/app/ApiDemos-debug.apk'
# 	dc['platformName'] = 'Android'
# 	dc['deviceName'] = 'Pixel 3 API 29'
# 	dc['automationName'] = 'UiAutomator2'
# 	dc["newCommandTimeout"] = 300
#
# 	if 'profile' in context.config.userdata.keys():
# 		if context.config.userdata['profile'] is None:
# 			profile = 'chrome'
# 		else:
# 			profile = context.config.userdata['profile']
# 	else:
# 		profile = 'chrome'
#
# 	if profile == 'chrome':
# 		context.driver = webdriver.Chrome()
# 	elif profile == 'firefox':
# 		context.driver = webdriver.Firefox()
# 	elif profile == 'android':
# 		context.driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
# 	else:
# 		context.driver = webdriver.Chrome()
# 		context.driver.maximize_window()
# 		context.driver.implicitly_wait(10)

def before_tag(context, tag):
	if tag == 'fixture.web':
		use_fixture(web, context)
	elif tag == 'fixture.mobile':
		use_fixture(mobile, context)


def after_scenario(context, scenario):
	context.driver.quit()
