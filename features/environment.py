from selenium import webdriver as webd
from appium import webdriver
from behave import fixture
from behave import use_fixture
import os
from datetime import datetime
from color_logs import *
from allure_behave.hooks import allure_report

color = ColorLogs()
device = ''

@fixture
def web(context):
	if 'profile' in context.config.userdata.keys():
		if context.config.userdata['profile'] is None:
			profile = 'chrome'
		else:
			profile = context.config.userdata['profile'].lower()
	else:
		profile = 'chrome'

	if profile == 'chrome':
		context.driver = webd.Chrome()
		print(color.format('start','===>Browser starts'))
	elif profile == 'firefox':
		context.driver = webd.Firefox()
		print(color.format('start','===>Browser starts'))
	else:
		print(color.format('fail', 'use one profile from the list: chrome, firefox'))
	context.driver.get("https://wi.zut.edu.pl")
	context.driver.maximize_window()
	context.driver.implicitly_wait(10)
	yield context.driver
	context.driver.quit()
	print(color.format('span','\nScenario time duration in seconds: '), context.scenario.duration)
	print(color.format('quit','===>Browser quits'))


@fixture
def mobile(context):
	dc = {}
	#global collect_session

	if 'profile' in context.config.userdata.keys():
		if context.config.userdata['profile'] is None:
			profile = 'android'
		else:
			profile = context.config.userdata['profile'].lower()
	else:
		profile = 'android'

	if profile == 'android':

		dc['app'] = os.getcwd()+'/app/ApiDemos-debug.apk'
		dc['platformName'] = 'Android'
		dc['deviceName'] = 'Pixel 3 API 29'
		dc['automationName'] = 'UiAutomator2'
		dc["newCommandTimeout"] = 300
		dc["clearDeviceLogsOnStart"] = True
		context.driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
		logs = context.driver.get_log("logcat")
		print(color.format('start','===>App starts'))
		time_start = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
		yield context.driver
		collect_android_log(context, logs, time_start)
		context.driver.quit()

	elif profile == 'ios':
		dc['app'] = ''
		dc['platformName'] = 'iOS'
		dc['platformVersion'] = ''
		dc['deviceName'] = ''
		dc['automationName'] = 'XCUITest'
		dc["newCommandTimeout"] = 300
		context.driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
		print(color.format('start', '===>App starts'))
		yield context.driver
		context.driver.quit()
	else:
		print(color.format('fail', 'use one profile from the list: android, ios'))

	print(color.format('span','\nScenario time duration in seconds: '), context.scenario.duration)
	print(color.format('quit', '===>App quits'))


def before_tag(context, tag):
	global device
	if tag == "fixture.mobile":
		device = "mobile"
	elif tag == "fixture.web":
		device = "web"


def before_scenario(context, scenario):
	if device == "mobile":
		use_fixture(mobile, context)
	elif device == "web":
		use_fixture(web, context)


def after_step(context, step):
	if step.status == 'failed':
		now = datetime.now()
		context.driver.save_screenshot(os.getcwd()+"/screenshots/"+step.name+now.strftime("%m_%d_%Y_%H_%M_%S")+".png")
		print("screenshot with failed saved in: "+os.getcwd()+"/screenshots/")


def before_all(context):
	allure_report(os.getcwd() + "allure/results")


def collect_android_log(context, logs, time_start):
	out_filename = os.getcwd() + "/android_logs/logfile_" + context.driver.capabilities.get(
		'deviceName') + "_" + time_start + ".log"
	f = open(out_filename, 'w', encoding='utf-8')
	adb_logs = list(map(lambda log: log['message'], logs))
	num = len(adb_logs)
	for i in range(num):
		f.write(adb_logs[i]+"\n")
	f.close()


