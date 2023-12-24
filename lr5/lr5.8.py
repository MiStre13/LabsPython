array = [21,24]

lamMap = lambda x: x % 7
numOst = list(map(lamMap, array))

for i in range(len(array)):
    print(f"Остаток от деления числа {array[i]} на 7: {numOst[i]}")