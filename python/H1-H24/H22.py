# def number_power(num, power):
#     if power == 1:
#         return num
#     if power == 0:
#         return 1
#     return num * number_power(num, (power-1))
# print(number_power(2,2))
# print(number_power(0,5))
# print(number_power(2,0))


# def fibonacci(num):
#     if num == 0 or num == 1:
#         return num
#     return fibonacci(num-1)+fibonacci(num-2)
# for i in range(10):
#     print(f"fibonacci({i}) - {fibonacci(i)}")


# def min_list_element(lst: list):
#     if len(lst) == 2:
#         return lst[0] if lst[0] <  lst[1] else lst[1]
#     return lst[0] if lst[0] < min_list_element(lst[1:]) else min_list_element(lst[1:])
# a = [11,2,3,4,5,6,7,8]
# print(min_list_element(a))


# def is_palindrom(s:str):
#     if len(s) == 1:
#         return True
#     if s[0] == s[-1]:
#         s = s[1:-1]
#         return is_palindrom(s)
#     return False
# print(is_palindrom("lol"))
# print(is_palindrom("low"))
# print(is_palindrom("l"))

