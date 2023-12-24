f = open('/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr7/lr3.txt','r')

for row in f:
    arr = row.split()
    arr = list(map(int, arr))
    arr = (f"Сумма строки = {sum(arr)}")
    print(arr)