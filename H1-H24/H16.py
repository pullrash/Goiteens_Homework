# 1
# tempringe_f = [14, 32, 212, 5]
# tempringe_c = list(map(lambda f: 5/9*(f-32),tempringe_f))
# print(tempringe_c)

# 2
# numbers = [1,2,3,4,5]
# squ_num = list(filter(lambda x: x%2==0, map(lambda x: x**2, numbers)))
# print(squ_num)

# 3
# text = "hello world im ostap"
# text_el = list(map(lambda x: len(x), list(text.split(" "))))
# print(text_el)

# 4
# names = ["maks","ostap","matviy","andriy","ostap"]
# uniq = []
# def uniq_name():
#     for i in names:
#         if i not in uniq:
#             uniq.append(i)
# uniq_name()
# final_names = list(map(lambda x: x + " Smith",uniq)) 
# print(final_names)       