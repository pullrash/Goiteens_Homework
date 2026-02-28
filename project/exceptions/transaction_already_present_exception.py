class TransactionAlreadyPresentException(Exception):
	def __init__(self, transaction_id: str):
		super().__init__(f'Transaction id {transaction_id} is already taken')