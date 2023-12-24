f = open('/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr7/lr1.txt','r')
arr = f.read()

arr = list(map(int, arr.split()))
print(f"Сумма чисел в файле = {sum(arr)}")
f.close()