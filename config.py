from selenium import webdriver
import unittest


class Template(unittest.TestCase):

        def setUp(self):
                self.driver = webdriver.Chrome()
                self.driver.get("https://wi.zut.edu.pl")
                self.driver.delete_all_cookies()
                self.driver.maximize_window()
        def TearDown(self):
                self.driver.quit()

