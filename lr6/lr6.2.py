numbersOne = input("Введите числа, разделенные пробелом для первого списка: ").split()
numbersTwo = input("Введите числа, разделенные пробелом для второго списка: ").split()
numbersSum = numbersOne + numbersTwo

digitsCountOne = {}
digitsCountTwo = {}
digitsCountSum = {}


for number in numbersOne:
    for count in str(number):
        if count in digitsCountOne:
            digitsCountOne[count] += 1
        else:
            digitsCountOne[count] = 1

for number in numbersTwo:
    for count in str(number):
        if count in digitsCountTwo:
            digitsCountTwo[count] += 1
        else:
            digitsCountTwo[count] = 1

for number in numbersSum:
    for count in str(number):
        if count in digitsCountSum:
            digitsCountSum[count] += 1
        else:
            digitsCountSum[count] = 1


# for digit, count in digitsCountOne.items():
#     print(f"Цифра в первом словаре {digit}: {count} раз(а)")

# for digit, count in digitsCountTwo.items():
#     print(f"Цифра во втором словаре {digit}: {count} раз(а)")

for digit, count in digitsCountSum.items():
    print(f"Цифра в обоих словарях {digit}: {count} раз(а)")




