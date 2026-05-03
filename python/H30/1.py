import random

list_num = []
for _ in range(10):
    list_num.append(random.randint(-10,100))
if all(n > 0 for n in list_num):
    print(sorted(list_num, reverse=True))
else:
    print("not all num > 0")