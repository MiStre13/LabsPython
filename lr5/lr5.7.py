def is_prime(n, circle=2):
    if n <= 1:
        return False
    if n == 2 or circle == n:
        return True
    if n % circle == 0:
        return False
    return is_prime(n, circle + 1)

num = int(input("Введите натуральное число: "))

if is_prime(num):
    print(f"Число {num} является простым")
else:
    print(f"Число {num} не является простым")
