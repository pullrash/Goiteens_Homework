from comands import transaction, payment_score, show
from comands import CommandsException

if __name__ == "__main__":
    while True:
        try:
            choise = int(input("веберіть дію ([1]Exit,[2]transaction,[3]payment,[4]show,[5]logging) "))
        except ValueError:
            choise = 0
        if choise == 1:
            break
        if choise == 2:
            try:
                a = input("input from_user ")
                b = input("input to_user ")
                c = int(input("input amount "))
                transaction(a,b,c)
            except CommandsException as e:
                print(f"eror: {e}")
            finally:
                print("operation was finished")
        if choise == 3:
            try:
                a = input("input user ")
                b = input("input payment_score ")
                payment_score(a,b)
            except CommandsException as e:
                print(f"eror: {e}")
            finally:
                print("operation was finished")
        if choise == 4:
            show()
