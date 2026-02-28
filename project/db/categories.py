categories = {}

def create_budget_tracker(category, budget):
    spent = 0
    def tracker(amount):
        nonlocal spent
        spent += amount
        if spent > budget:
            print(f"Бюджет перевищено у категорії {category}! Витрачено: {spent}, Ліміт: {budget}")
        else:
            print(f"Витрати у категорії {category}: {spent}/{budget}")
    return tracker