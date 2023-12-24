a = int(input("Введите число: "))
revNum = 0
whDigit = a

while whDigit != 0:
        digit = whDigit % 10
        revNum = revNum * 10 + digit
        whDigit //= 10
print("Число слева направо: ",revNum)