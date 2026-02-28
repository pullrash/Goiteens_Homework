from datetime import datetime, timedelta

def days_until_end_of_month():
	today = datetime.today()
	next_month = today.replace(day=28) + timedelta(days=4)
	end_of_month = next_month - timedelta(days=next_month.day)
	return (end_of_month - today).days

def calculate_budget_remaining(budget, spent):
	try:
		days_left = days_until_end_of_month()
		daily_budget = (budget - spent) / days_left
		return daily_budget, days_left
	except ZeroDivisionError:
		print("Сьогодні останій день")
def days_until_end_of_week():
	today = datetime.now()
	end_of_week = today + timedelta(days=(6-today.weekday()))
	return (end_of_week - today).days