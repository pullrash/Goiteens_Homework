class UserAlreadyExistsException(Exception):
	def __init__(self, username):
		super().__init__(f'This username is already taken: {username}')