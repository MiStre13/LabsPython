a = int(input("Введите число: "))
revNum = 0
whDigit = a

if 1000>a>99:
    while whDigit != 0:
        digit = whDigit % 10
        revNum = revNum * 10 + digit
        whDigit //= 10

    if a == revNum:
        print("Является палиндромом",revNum, a)
    else:
        print("Не является палиндромом",revNum, a)
else:
    print("Надо ввести 3-х значное число")


