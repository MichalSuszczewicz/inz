class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def platformName(self):

        platform = self.driver.capabilities.get('platformName')

        return platform
