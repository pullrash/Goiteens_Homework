import os
from config import users, users_bill, LOG_FILE
class CommandsException(Exception):
    pass

def transaction(from_user, to_user, amount):
    from_user = from_user.capitalize()
    to_user = to_user.capitalize()
    if from_user not in users or to_user not in users:
        raise CommandsException("невірно введені данні користувачів")
    if amount < 0:
        raise CommandsException("невірна сума")
    if amount > users[from_user]:
        raise CommandsException("недостатньо коштів")
    users[from_user] -= amount
    users[to_user] += amount


def payment_bill(user, score):
    user = user.capitalize()
    if user not in users:
        raise CommandsException("незнайдено користувача")
    if score not in users_bill:
        raise CommandsException("рахунок не знайдено")
    if users[user] < users_bill[score]:
        raise CommandsException("недостатньо коштів")
    users[user] -= users_bill[score]
    users_bill[score] = 0

def show():
    for user, balance in users.items():
        print(user, balance)
    for score, value in users_bill.items():
        print(score, value)

def show_logs():
    print("Історія операцій")
    if not os.path.exists(LOG_FILE):
        print("Файл логів ще не створено.")
        return
    
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        logs = file.readlines()
        if not logs:
            print("Логи порожні.")
        else:
            for line in logs:
                print(line.strip())
    print("-"*20,"\n")