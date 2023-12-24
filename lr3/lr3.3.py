a = int(input("Введите число а "))
b = int(input("Введите число b "))
i = 1
if b>=a:
    # a**2+2*a*b+b**2
    while i<=b:
        i+=1
        sum = (a-i)**2+2*a*i
        print(sum)

else:
    print("b должно быть больше a")

(1^2+2^2+3^2+4^2+5^2)