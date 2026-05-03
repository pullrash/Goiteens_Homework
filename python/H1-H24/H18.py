text = input("Введіть текст ")
text = list(text)
leters = set(text)
leters.discard(" ")
res = []
count = 0
for i in leters:
    count = 0
    for j in text:
        if i == j:
            count += 1
    res.append(str(count)+ i)
    res.sort()
final_res = res[-1:-4:-1]
print("найбільше {:<0} потім {:<0} потім {:<0}".format(final_res[0],final_res[1],final_res[2],))          