gr17 = ["Дима","Вася","Коля","Алена"]
gr18 = ["Костя","Наташа","Лера"]
gr19 = ["Миша","Илья"]

allPeople = sorted(gr17 + gr18 + gr19)
print("Общее кол-во человек во всех группах", len(allPeople))

if len(gr17) > len(gr18) > len(gr19):
    print("В группе 17 больше человек", len(gr17))
elif len(gr17) < len(gr18) > len(gr19):
    print("В группе 18 больше человек", len(gr18))
elif len(gr17) < len(gr18) < len(gr19):
    print("В группе 19 больше человек", len(gr19))

if len(gr17) > len(gr18) > len(gr19):
    print("В группе 19 меньше человек", len(gr19))
elif len(gr17) > len(gr18) < len(gr19):
    print("В группе 18 меньше человек", len(gr18))
elif len(gr17) < len(gr18) < len(gr19):
    print("В группе 17 меньше человек", len(gr19))


print("Вывод учеников по алфавиту")
for i in range(len(allPeople)):
    print(i+1, allPeople[i])
    
