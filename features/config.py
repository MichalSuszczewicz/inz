from selenium import webdriver
import unittest
import argparse


class Template():

        driver = webdriver.Chrome

     #   def close(context):
           #     context.driver.close()

        # parser = argparse.ArgumentParser(description="choose browser")
        # parser.add_argument('--chrome')
        # parser.add_argument('--firefox')
        #
        # device = parser.parse_args()


        # def setUp(self, device):
        #         if device == "--firefox":
        #                 self.driver = webdriver.Firefox()
        #         elif device == "--chrome":
        #                 self.driver = webdriver.Chrome()
        #         else:
        #                 self.driver = webdriver.Chrome()
        #         self.driver.get("https://wi.zut.edu.pl")
        #         self.driver.delete_all_cookies()
        #         self.driver.maximize_window()
        #
        # def TearDown(self):
        #         self.driver.quit()
