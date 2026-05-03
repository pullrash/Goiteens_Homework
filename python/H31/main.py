from config import LOG_FILE
import logging
from comands import transaction, payment_bill, show, show_logs
from comands import CommandsException

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8")
    ]
)


if __name__ == "__main__":
    logging.info("Сесія банкомату розпочата.")
    
    while True:
        try:
            choice = int(input("Виберіть дію ([1]Exit, [2]transaction, [3]payment, [4]show, [5]logging): "))
        except ValueError:
            choice = 0

        if choice == 1:
            logging.info("Користувач вийшов з програми.")
            break

        if choice == 2:
            try:
                a = input("input from_user: ")
                b = input("input to_user: ")
                c = int(input("input amount: "))
                transaction(a, b, c)
                logging.info(f"Успішний переказ: {a} -> {b} (сума: {c})")
            except CommandsException as e:
                logging.error(f"Помилка транзакції {a}->{b}: {e}")
                print(f"error: {e}")
            except ValueError:
                logging.warning("Спроба введення тексту замість суми в транзакції.")
                print("error: сума має бути числом")
            finally:
                print("operation was finished")

        elif choice == 3:
            try:
                a = input("input user: ")
                b = input("input payment_score: ")
                payment_bill(a, b)
                logging.info(f"Успішна оплата: користувач {a}, рахунок {b}")
            except CommandsException as e:
                logging.error(f"Помилка оплати ({a}, рахунок {b}): {e}")
                print(f"error: {e}")
            finally:
                print("operation was finished")

        elif choice == 4:
            show()
            logging.info("Користувач переглянув стан рахунків.")

        elif choice == 5:
            show_logs()