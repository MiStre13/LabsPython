a = int(input("Введите число: "))


if a>99:
    e = a%100//10
    d = a//100
    n = (e*100+d*10+a%10)
    print("Новое число", n)
 
else:
    print("Надо ввести 3-х значное число")
