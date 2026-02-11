# розпізнавання в якій чверті буде точка

x = float(input("ведіть координату x "))
y = float(input("ведіть координату y "))
if x > 0 and y > 0:
    print("це перша чверть")
elif x < 0 and y > 0:
    print("це друга чверть")
elif x < 0 and y < 0:
    print("це третя чверть")
elif x > 0 and y < 0:
    print("це четверта чверть")
elif x == 0 and y != 0:
    print("точка належить осі y")
elif x != 0 and y == 0:
    print("точка належить осі x")
else:
    print("такої координати не існує")

# чи склала людина іспит

surname = input("ведіть своє прізвище ")
grade = int(input("ведіть свій бал "))
if surname and grade >= 80:
    print(f"{surname} здав іспит")
elif surname and grade < 80:
    print(f"{surname} не здав")
else:
    print("введені неправильні данні")