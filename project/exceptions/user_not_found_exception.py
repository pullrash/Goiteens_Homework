class UserNotFoundException(Exception):
	def __init__(self, username):
		super().__init__(f'User not found by name: {username}')