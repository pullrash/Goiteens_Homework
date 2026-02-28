from datetime import datetime, timedelta

def filter_transactions_by_date(transactions: dict, start_date: datetime, end_date: datetime):
	for transaction_id, details in transactions.items():
		transaction_date = datetime.strptime(details['date'], '%Y-%m-%d')
		if start_date <= transaction_date <= end_date:
			yield transaction_id, details

def generate_monthly_report(transactions, year, month):
	start_date = datetime(year, month, 1)
	end_date = start_date + timedelta(days=32)
	end_date = end_date.replace(day=1) - timedelta(days=1)

	report = []
	total_income = 0
	total_expenses = 0

	for transaction_id, details in filter_transactions_by_date(transactions, start_date, end_date):
		date = details['date']
		amount = details['amount']
		category = details['category']

		report.append(f'ID: {transaction_id}, Дата: {date}, Сума: {amount}, Категорія: {category}')

		if amount > 0:
			total_income += amount
		else:
			total_expenses += abs(amount)
	
	report_summary = f"\nЗвіт за {year}-{month}:\n"
	report_summary += f"Загальний дохід: {total_income}\n"
	report_summary += f"Загальні витрати: {total_expenses}\n"
	report_summary += f"Чистий дохід: {total_income - total_expenses}\n"
	
	return '\n'.join(report) + report_summary

def export_to_file(report, file_path):
	with open(file_path, 'w', encoding='utf-8') as file:
		file.write(report)
	print(f"Звіт успішно збережено у файл {file_path}")