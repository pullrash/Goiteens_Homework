class InvalidInputException(Exception):
	def __init__(self, message="Некоректне введення. Очікується число."):
		super().__init__(message)