from exceptions.currency_not_found_exception import CurrencyWasNotFoundException

exchange_rates = {
    'USD': 1.0,
    'EUR': 1.1817,
    'UAH': 0.0231
}

def get_available_currencies() -> set:
	return exchange_rates.keys()

def exchange_to_usd(amount: float, currency: str) -> float:
	if exchange_rates.get(currency) is None:
		raise CurrencyWasNotFoundException(currency)
	return amount * exchange_rates[currency]