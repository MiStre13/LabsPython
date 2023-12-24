import random
array = [random.randrange(1,100) for i in range(10)]
# array = [1,2,3,4,5,6,7,8,9,10]
newArrayChet = []
newArrayNull = []


for i in range(len(array)):
    if array[i] % 2 == 0:
        print("Четные число", array[i])
        newArrayChet.append(array[i])

    if array[i] % 10 == 0:
        newArrayNull.append(array[i])

print("Массив из четных цифр",newArrayChet)
print("Массив из цифр c 0 вконце",newArrayNull)



