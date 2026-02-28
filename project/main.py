from services.reports import generate_monthly_report, export_to_file
from services.auth_service import *
from db.transactions import *
from db.users import *
from services.reports import *
from services.budget import calculate_budget_remaining

def main():
	while True:
		print('Hello user!')
		choise = input("виберіть дію (reg, log, exit) ").lower().strip()
		if choise == "reg":
			username = input("Введіть логін: ")
			password = input("Введіть пароль: ")
			forgot_password = input("Введіть відповідь питання на випадок якщо забудете пароль, щоб змінити його: \nЯк звати вашу домашню тваринку? ")
			register_user(username, password)
		elif choise == "log":
			username = input("Введіть логін: ")
			password = input("Якщо забули пароль напишіть forgot\nВведіть пароль: ").lower().strip()
			if password == "forgot":
				print("Щоб змінити пароль дайте відповідь на питання:\nЯк звати вашу домашню тваринку?")
				user_answer = input("")
				if user_answer == forgot_password:
					password = input("Введіть новий пароль: ")
					change_password(username, hash_password(password))
				else:
					print("Неправильно")
		elif choise == "exit":
			break
		try:
			if authenticate_user(username, password):
				while True:
					command = input("Введіть команду (add, edit, delete, calc, budget, balance, report, back): ").lower().strip()
					if command == "add":
						transaction_id = create_transaction_id()
						print(f"ID цієї транзакції: {transaction_id}")
						amount = float(input("Введіть суму: "))
						date = input("Введіть дату (YYYY-MM-DD): ")
						category = input("Введіть категорію: ")
						currency = input('currency ').upper()
						add_transaction(transaction_id, amount, currency, date, category)
					elif command == "edit":
						transaction_id = input("Введіть ід транзакції ")
						amount = float(input("Введіть суму: "))
						date = input("Введіть дату (YYYY-MM-DD): ")
						category = input("Введіть категорію: ")
						currency = input('currency ').upper()
						edit_transaction(transaction_id, amount, currency, date, category)
					elif command == "delete":
						transaction_id = input("Введіть ід транзакції ")
						delete_transaction(transaction_id)
					elif command == "calc":
						category = input("Введіть категорію (не обов'язково) ")
						calculate_total(category)
					elif command == "budget":
						budget = float(input("Введіть бюджет на місяць: "))
						spent = float(input("Введіть витрачені кошти: "))
						calculate_budget_remaining(budget, spent)
					elif command == "balance":
						view_balance()
					elif command == "report":
						now = datetime.now()
						report = generate_monthly_report(transactions, now.year, now.month)
						export_to_file(report, 'report.txt')
					elif command == "back":
						print("Повертаєсомь до регістрації користувача")
						break
					else:
						print("Невідома команда. Спробуйте ще раз.")
		except UserNotFoundException as e:
			print(e)
		except InvalidPasswordException as e:
			print(e)



if __name__ == '__main__':
	main()