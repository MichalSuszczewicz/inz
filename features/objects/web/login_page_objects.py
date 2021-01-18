class LoginPageObjects():
	def __init__(self):
		self.login_input = {'css_selector': '','xpath': '//*[@id="username"]'}
		self.password_input = {'css_selector': '', 'xpath': '//*[@id="password"]'}
		self.log_in_button = {'css_selector': '', 'xpath': '//*[@id="main-content"]/div[2]/form/fieldset/div[4]/div/button'}
		self.login_form = {'css_selector': '', 'xpath':'//*[@id="main-content"]/div[2]/form'}
		self.error_field = {'css_selector': '', 'xpath': '//*[@id="system-message"]'}
		self.error = {'css_selector': '', 'xpath': '//*[@id="system-message"]/div/div/div'}
