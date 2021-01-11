class ColorLogs:
	HEADER = '\033[96m'
	LIGHTBLUE = '\033[94m'
	WARNING = '\033[93m'
	FAIL = '\033[31m'
	ENDLINE = '\033[0m'
	UNDERLINE = '\033[4m'

	def format(self, color, text):
		output = ''

		if  color == 'quit':
			output = self.LIGHTBLUE + text + self.ENDLINE
		elif color == 'fail':
			output = self.FAIL + text + self.ENDLINE
		elif color == 'warning':
			output = self.WARNING + text + self.ENDLINE
		elif color == 'span':
			output = self.UNDERLINE + text + self.ENDLINE
		elif color == 'start':
			output = self.HEADER + text + self.ENDLINE

		return output