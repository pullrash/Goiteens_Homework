from config import users, users_score
class CommandsException(Exception):
    pass

def transaction(from_user, to_user, amount):
    from_user = from_user.capitalize()
    to_user = to_user.capitalize()
    if from_user not in users or to_user not in users:
        raise CommandsException("невірно введені данні користувачів")
    if amount < 0:
        raise CommandsException("невірна сума")
    if amount > users[from_user]["balance"]:
        raise CommandsException("недостатньо коштів")
    users[from_user]["balance"] -= amount
    users[to_user]["balance"] += amount


def payment_score(user, score):
    user = user.capitalize()
    if user not in users:
        raise CommandsException("незнайдено користувача")
    if score not in users_score:
        raise CommandsException("рахунок не знайдено")
    if users[user]["balance"] < users_score[score]:
        raise CommandsException("недостатньо коштів")
    users[user]["balance"] - users_score[score]
    users_score[score] = 0

def show():
    for user, balance in users.items():
        print(user, balance)
    for score, value in users_score.items():
        print(score, value)