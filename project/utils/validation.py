from exceptions.out_of_range_exception import OutOfRangeException

def get_user_input(prompt: str, min_value=None, max_value=None, repeat=True):
	if repeat:
		while True:
			try:
				return get_validated_user_input(prompt, min_value, max_value)
			except ValueError:
				print("Помилка: Очікується числове значення.")
			except OutOfRangeException as e:
				print(f"Помилка: {e}")
	
	try:
		return get_validated_user_input(prompt, min_value, max_value)
	except ValueError:
		print("Помилка: Очікується числове значення.")
	except OutOfRangeException as e:
		print(f"Помилка: {e}")

def get_validated_user_input(prompt: str, min_value=None, max_value=None):
	value = float(input(prompt))
	if min_value is not None and value < min_value:
		raise OutOfRangeException()
	elif max_value is not None and value > max_value:
		raise OutOfRangeException()
	return value