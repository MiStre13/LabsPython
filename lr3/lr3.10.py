n = int(input("Введите число: "))
digits = []
while n > 0:
    digit = n % 10
    digits.insert(0, digit)
    n = n // 10
    print(digits)

min_digit = min(digits)
max_digit = max(digits)

if digits.index(min_digit) < digits.index(max_digit):
    print("Минимальная левее")
    print(min_digit)
else:
    print("Максимальная левее")
    print(max_digit)
