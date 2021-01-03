class BasePage(object):
    def __init__(self, driver):
       # self.base_url = base_url
        self.driver = driver
        self.timeout = 30
