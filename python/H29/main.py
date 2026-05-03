list_tasks = [
    {"name":"to hoover", "time":20},
    {"name":"to mop", "time":15},
    {"name":"fo homework", "time":40},
    {"name":"to dust", "time":20},
    {"name":"wash the dishes", "time":15},
    {"name":"take the trash", "time":5}
]
print(sorted(list_tasks, key=lambda task: (task["time"], task["name"]), reverse=True))


import random

list_num = []
for _ in range(10):
    list_num.append(random.randint(-10,100))
if all(n > 0 for n in list_num):
    print(sorted(list_num, reverse=True))
else:
    print("not all num > 0")