from db.users import *
from exceptions.user_not_found_exception import UserNotFoundException
from exceptions.user_already_exists_exception import UserAlreadyExistsException
from exceptions.invalid_password_exception import InvalidPasswordException
import hashlib

def hash_password(password: str) -> str:
	return hashlib.sha256(password.encode()).hexdigest()

def register_user(username: str, password: str):
    if is_user_in_db(username):
        raise UserAlreadyExistsException(username)
    add_user(username, hash_password(password)) 

def authenticate_user(username: str, password: str) -> bool:
    if not is_user_in_db(username):
        raise UserNotFoundException(username)
    if get_user_password(username) != hash_password(password):
        raise InvalidPasswordException()
    return True