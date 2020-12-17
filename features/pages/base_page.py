class BasePage(object):
    def __init__(self, browser, base_url='https://wi.zut.edu.pl'):
        self.driver = browser
        self.base_url = base_url
