f = open('/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr7/lr2.txt','r')
inputSymbol = input("Введите символ для проверки ")

for i in f:
    if i == inputSymbol:
        info = (f"Символ {inputSymbol} есть в файле")
    else:
        info = (f"Символ {inputSymbol} отсуствует в файле")

print(info)

f.close()

