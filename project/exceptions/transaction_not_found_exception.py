class TransactionNotFoundException(Exception):
	def __init__(self, transaction_id):
		super().__init__(f'Transaction not found by id: {transaction_id}')