a = int(input("Введите число: "))
revNum = 0
whDigit = a

if a>99:
    while whDigit != 0:
        digit = whDigit % 10
        revNum = revNum * 10 + digit
        whDigit //= 10
    print("Число слева направо = ",revNum)
else:
    print("Надо ввести 3-х значное число")


