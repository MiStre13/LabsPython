def decimal_to_n(num, base):
    digits = "0123456789ABCDEF"
    if num < base:
        print(digits[num])
        return digits[num]
    else:
        return decimal_to_n(num // base, base) + digits[num % base]


num = int(input("Введите число в десятичной системе: "))
base = int(input("Введите  систему счисления: "))
result = decimal_to_n(num, base)

print(f"Число {num} в системе счисления с {base} системой счисления: {result}")
