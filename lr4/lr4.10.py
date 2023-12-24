l = [1, 2, 3, 4, 5, 6, 7]  
 
k1 = int(input("Введите k1"))
k2 = int(input("Введите k2"))
 
l = l[k2:] + l[k1:k2] + l[:k1]
print(l)