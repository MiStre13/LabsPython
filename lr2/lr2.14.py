a = int(input("Введите число: "))
lastDigit = a % 10
if lastDigit%2==0:
    print("Оканчивается четной цифрой")
else:
    print("Не оканчивается четной цифрой")