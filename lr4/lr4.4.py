a = [1,2,3,4,5,6]
p = 1
s = 0

for i in range(len(a)):
    s = s+p*a[i]
    p = -p

print("Ответ:",s)