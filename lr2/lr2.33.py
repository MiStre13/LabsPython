def func_test(a, b, c : int =None):
    if (a<50 and b>=50 and c>=50) or (a>=50 and b<50 and c>=50) or (a>=50 and b>=50 and c<50):
        print("TRUE")
        return 0
    print("FALSE")

alph = ("Введите буквку условия от А до Е")


if alph == "A":
    print("а) каждое из чисел А и В больше 100;")

    a=int(input("Введи число A ="))
    b=int(input("Введи число B ="))

    if a>100 and b > 100:
        print("Условие верно")
    else:
        print("Условие не верно")


elif alph == "B":

    print("б) только одно из чисел А и В четное;")

    a=int(input("Введи число A ="))
    b=int(input("Введи число B ="))

    if a%2==0 or b%2==0:
        print("Одно из чисел четное")
    else:
        print("Оба числа четны или оба числа нечетные")


elif alph == "C":

    print("в)  хотя бы одно из чисел А и В положительно;")

    a=int(input("Введи число A ="))
    b=int(input("Введи число B ="))

    if a>0 or b>0:
        print("Одно из чисел положительно")
    else:
        print("Оба числа отрицательны или оба числа положительны")

elif alph == "G":

    print("г)  хотя бы одно из чисел А и В положительно;")

    a=int(input("Введи число A ="))
    b=int(input("Введи число B ="))
    c=int(input("Введи число С ="))

    if a%3==0 and b%3==0 and c%3==0:
        print("Все числа кратны 3-м")
    else:
        print("Все или одно из чисел не кратно трем")

elif alph == "D":

    print("д) только одно из чисел А, В и С меньше 50; ")

    a=int(input("Введи число A ="))
    b=int(input("Введи число B ="))
    c=int(input("Введи число С ="))

    func_test(a, b, c)
    # list_data = [a, b, c]
    # counter = 0
    # for i in list_data:
    #     if i < 50:
    #         counter += 1
    # if counter == 1:
    #     print("True")
    # else:
    #     print("False")

    
elif alph == "E":
    print("е) хотя бы одно из чисел А, В, С отрицательно ")

    a=int(input("Введи число A ="))
    b=int(input("Введи число B ="))
    c=int(input("Введи число С ="))

    if a<0 or b<0 or c<0:
        print("TRUE")
    else: 
        print("FALSE")

else:
    print("Такого номера нет в списке")


