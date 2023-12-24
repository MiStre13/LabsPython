import math

n = int(input("Введите факториал: "))
digit = 1
while n>1:
    digit += 1
    n = n/digit
print("Число факториала =",digit)
fac = math.factorial(digit)
print("Проверка Факториала: ",fac)

