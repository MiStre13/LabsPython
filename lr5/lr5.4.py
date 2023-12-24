def gcd_three_numbers(a, b, c):
    gcd_ab = gcd(a,b)
    gcd_abc = gcd(gcd_ab, c)
    return gcd_abc

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

a = int(input("Введите число a"))
b = int(input("Введите число b"))
c = int(input("Введите число c"))
print(gcd_three_numbers(a, b, c))