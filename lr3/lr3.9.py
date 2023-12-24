n = int(input("Введите число для проверки: "))
s = int(input("Введите шаг прогрессии: "))
f = int(input("Введите первый член прогрессии: "))

check_num = f
while check_num <= n:
    if check_num == n:
        print("число ",n,"является членом прогрессии")
        break
    check_num += s
else:
    print("число ",n,"не является членом прогрессии")
