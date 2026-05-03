name_table = ["1 столик","2 столик","3 столик","4 столик","5 столик"]
def reserv(surname,count = 2):
    if surname != 0 :
        if len(name_table[0]) == 8 and surname != 1:
            name_table[0] += f" заброньовано на {surname} на {count} людини"
        elif len(name_table[1]) == 8 and surname != 1:
            name_table[1] += f" заброньовано на {surname} на {count} людини"
        elif len(name_table[2]) == 8 and surname != 1:
            name_table[2] += f" заброньовано на {surname} на {count} людини"
        elif len(name_table[3]) == 8 and surname != 1:
            name_table[3] += f" заброньовано на {surname} на {count} людини"
        elif len(name_table[4]) == 8 and surname != 1:
            name_table[4] += f" заброньовано на {surname} на {count} людини"
        for i in range(5):
            print("-"* 50)
            print("|{:48}|".format(name_table[i]))
        
    else:
        if len(name_table[4]) != 8:
            print("Всі столики зайняті!")
            return 0
while True:
    a = input("бажаєте замовити столик? ").lower()
    if a == "так" and reserv(0) != 0:
        surname = input("на чиє прізвище? ").capitalize()
        count = input("на скільки осіб? ")
        reserv(surname,count)
    else:
        reserv(1)
        break