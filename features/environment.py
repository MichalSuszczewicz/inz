from selenium import webdriver
from features.config import Template

def before_feature(self, context):

    context.browser = Template()

def after_feature(self, context):
    context.browser.quit()