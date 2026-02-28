from exceptions.transaction_already_present_exception import TransactionAlreadyPresentException
from exceptions.transaction_not_found_exception import TransactionNotFoundException
from utils.exchange import exchange_to_usd

transactions = {}

def create_transaction_id(x=1):
	if not is_transaction_present(x):
		return str(x)
	else:
		x += 1
		create_transaction_id(x)

def is_transaction_present(transaction_id: str):
	return transaction_id in transactions.keys()

def add_transaction(transaction_id: str, amount: float, currency: str, date, category):
	if is_transaction_present(transaction_id):
		raise TransactionAlreadyPresentException(transaction_id)
	
	transactions[transaction_id] = {
		'amount': exchange_to_usd(amount, currency),
		'date': date,
		'category': category
	}

def edit_transaction(transaction_id: str, amount: float = None, currency: str = None, date = None, category = None):
	if not is_transaction_present(transaction_id):
		raise TransactionNotFoundException(transaction_id)
	
	if amount:
		transactions[transaction_id]['amount'] = exchange_to_usd(amount, currency)
	if date:
		transactions[transaction_id]['date'] = date
	if category:
		transactions[transaction_id]['category'] = category

def delete_transaction(transaction_id):
	if not is_transaction_present(transaction_id):
		raise TransactionNotFoundException(transaction_id)
	
	del transactions[transaction_id]

def calculate_total(category=None, index=0, total=0):
    keys = list(transactions.keys())
    if index == len(keys):
        return total
    if category:
        if transactions[keys[index]]['category'] == category:
            total += transactions[keys[index]]['amount']
    else:
        total += transactions[keys[index]]['amount']
    return calculate_total(category, index + 1, total)