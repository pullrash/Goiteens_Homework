from exceptions.user_not_found_exception import UserNotFoundException
from exceptions.user_already_exists_exception import UserAlreadyExistsException
from db.transactions import transactions

users_db = {}

def is_user_in_db(username: str) -> bool:
	return username in users_db.keys()

def get_user_password(username: str) -> str:
	if not is_user_in_db(username):
		raise UserNotFoundException(username)
	return users_db.get(username)

def add_user(username: str, hashed_password: str):
	if is_user_in_db(username):
		raise UserAlreadyExistsException(username)
	users_db[username] = hashed_password

def change_password(username: str, hashed_password: str):
	users_db[username] = hashed_password

def view_balance():
    balance = sum(t['amount'] for t in transactions.values())
    print(f"Ваш поточний баланс: {balance}")