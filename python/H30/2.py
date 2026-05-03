import os, sys, datetime

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = input("Введіть шлях до папки: ")

os.chdir(path)

while True:
    print(f"\n--- Вміст папки: {os.getcwd()} ---")
    
    files = os.listdir('.')
    for file in files:
        stats = os.stat(file)
        size = stats.st_size
        mtime = datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M')
        
        type_label = "[DIR]" if os.path.isdir(file) else "[FILE]"
        print(f"{type_label} {file:20} | {size:10} байт | {mtime}")

    print("\nОберіть дію: [1] Перейменувати [2] Видалити [3] Нова папка [4] Вихід")
    choice = input("Ваш вибір: ")

    if choice == '1':
        old = input("Що перейменувати? ")
        new = input("Нова назва: ")
        os.rename(old, new)
    
    elif choice == '2':
        name = input("Назва файлу для видалення: ")
        os.remove(name)
    
    elif choice == '3':
        folder = input("Назва нової папки: ")
        os.mkdir(folder)
    
    elif choice == '4':
        print("Завершення роботи.")
        sys.exit()