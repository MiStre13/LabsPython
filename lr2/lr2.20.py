a = int(input("Введите число: "))


if a>99:
    a=a//100 + a % 100 * 10
    print("Число:", a)
else:
    print("Надо ввести 3-х значное число")