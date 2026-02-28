class InvalidPasswordException(Exception):
	def __init__(self):
		super().__init__('Your password is invalid')