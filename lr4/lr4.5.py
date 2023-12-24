import random
count = 42
classCount = [random.randrange(10,30) for i in range(count)]
classCountSum = sum(classCount)


if len(str(classCountSum))==4: 
    print("Общее число учеников 4-х значное число",classCountSum)
else:
    print("Общее число учеников не 4-х значное число",classCountSum)

#Тестовая информация
# print(classCountSum)
# print(classCount)
# print(len(classCount))