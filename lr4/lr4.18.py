list = [i for i in range(1,21)]
newList = []
listChet = []
listNechet = []

for i in range(len(list)):
    if list[i]%2==0:
        list[i] *= list[i]
        newList.append(list[i])
        listChet.append(list[i])
    elif list[i]%2 != 0:
        list[i] += 2
        newList.append(list[i])
        listNechet.append(list[i])

print("полный массив",newList)

print("четные", listChet)
print("нечетные", listNechet)