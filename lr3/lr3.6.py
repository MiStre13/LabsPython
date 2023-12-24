
numbers = []

while True:
    try:
        number = int(input("Введите число (или букву для окончания ввода): "))
        numbers.append(number)
    except ValueError:
        break
print("Введенные числа:", numbers)


count = 0
index = 0
while(numbers[index]<0):
   count+=1
   index+=1
print(count)