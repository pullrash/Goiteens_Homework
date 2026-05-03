# 1.Написати програму, яка буде підраховувати суму всіх непарних чисел від 1 до 100.

# sum = 0
# for i in range(1,101):
#     print(i)
#     if i % 2 == 1:
#         sum += i
# print(f"sum = {sum}")

# або простіше

# sum = 0
# for i in range(1,101,2):
#     sum += i
#     print(i)
# print(f"sum = {sum}")

#2. Написати програму, яка приймає на вхід рядок, введений з клавіатури, і підраховує кількість входження в рядок першої літери, з якої починається цей рядок.

# text = input("Введи текст ")
# sum = 0
# first_liter = ""
# for i in text:
#     first_liter += i
#     break
# for i in text:
#     if i == first_liter:
#         sum += 1
# print(f"в {text} {first_liter} зустрічається {sum} разів")

# або коротше

# text = input("Введи текст ")
# sum = 0
# first_liter = text[0]
# for i in text:
#     if i == first_liter:
#         sum += 1
# print(f"в {text} {first_liter} зустрічається {sum} разів")