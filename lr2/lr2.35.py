

alph = input("Выберете пункт A or B ")

if alph=="A":
    x=int(input("Введите координату x "))
    y=int(input("Введите координату y "))

    if x<= -1 and y<=-2:
        print("Попал на участок")
    else:
        print("Не попал на участок")

elif alph=="B":
    x=int(input("Введите координату x "))
    y=int(input("Введите координату y "))

    if y>=1 or y<=-3:
        print("Попал на участок")
    else:
        print("Не попал на участок")

else:
    print("Нужно выбрать А или В")