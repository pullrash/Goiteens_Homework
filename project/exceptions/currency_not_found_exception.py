class CurrencyWasNotFoundException(Exception):
	def __init__(self, currency):
		super().__init__(f'Exchange currency {currency} was not found')