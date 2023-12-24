numbers = input("Введите числа, разделенные пробелом: ").split()
digits_count = {}

for number in numbers:
    for count in str(number):
        if count in digits_count:
            digits_count[count] += 1
        else:
            digits_count[count] = 1

print("Количество повторений различных цифр:")

for digit, count in digits_count.items():
    print(f"Цифра {digit}: {count} раз(а)")
