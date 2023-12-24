a = int(input("Введите a "))
p = int(input("Введите p "))
arr = [a]
for i in range(1, 10):
    arr.append(a+i*p)
print(arr)