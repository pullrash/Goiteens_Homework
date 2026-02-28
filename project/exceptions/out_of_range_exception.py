class OutOfRangeException(Exception):
	def __init__(self, message="Число виходить за межі допустимого діапазону."):
		super().__init__(message)