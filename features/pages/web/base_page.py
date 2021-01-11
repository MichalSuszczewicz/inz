class BasePage(object):
    def __init__(self, driver, base_url='https://wi.zut.edu.pl'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    # def find_element(self, *loc):
    #     return self.driver.find_element(*loc)

