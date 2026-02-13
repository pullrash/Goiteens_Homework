import random, sys

while True:
    print("\n--- ГЕНЕРАТОР ВИПАДКОВИХ ПОДІЙ ---")
    print("1. Кинути кубик")
    print("2. Обрати переможця зі списку")
    print("3. Згенерувати послідовність чисел")
    print("4. Вийти")
    
    choice = input("\nОберіть варіант (1-4): ")

    if choice == '1':
        print(f"Результат: {random.randint(1,6)}")

    elif choice == '2':
        data = input("Введіть імена учасників через кому: ")
        names = data.split(",") 
        winner = random.choice(names)
        print(f"Переможець: {winner.strip()}")

    elif choice == '3':
        count = int(input("Скільки чисел згенерувати? "))
        limit = int(input("До якого числа (максимум)? "))
        numbers = random.sample(range(1, limit + 1), count)
        print(f"Ваша послідовність: {numbers}")

    elif choice == '4':
        print("Бувай!")
        sys.exit()
    
    else:
        print("Неправильний вибір!")