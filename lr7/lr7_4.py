file = open('/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr7/lr4.txt','r')
lst = file.read().split()
summ=0
num_lines=0
with open ('/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr7/lr4.txt') as f: 
    num_lines = len(f.readlines ())

for i in lst:
    summ+=len(i)
print(f"Количесвто слов:{len(lst)} Количество букв: {summ} Количество строк:{num_lines}")
