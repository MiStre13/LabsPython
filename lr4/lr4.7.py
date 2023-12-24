import random
scoreRus = [random.randrange(1,100) for i in range(1,11)]
scoreEng = [random.randrange(1,100) for i in range(1,11)]
scoreInfo = [random.randrange(1,100) for i in range(1,11)]
nameStudent = ["Dima", "Mikhail", "Vasi", "Lera", "Natasha", "Misha", "Artem", "Kirill", "Dima", "Kostya"]
sumScoreArr = []
winArr = []
circle = []

scoreWin = int(input("Введите проходной балл:"))
# scoreWin = 200


for i in range(len(scoreRus)):
    sumScoreArr.append(scoreRus[i] + scoreEng[i] + scoreInfo[i])
    if sumScoreArr[i] > scoreWin:
        winArr.append(sumScoreArr[i])
        circle.append(i)
        # for i in range(len(winArr)):
        #     resul_list = [nameStudent[i] for i in circle]
        #     print(resul_list[i],":",winArr[i],"балл")
    else: 
        print(nameStudent[i],"не прошел")

# print(sumScoreArr)
for i in range(len(winArr)):
     resul_list = [nameStudent[i] for i in circle]
     print(resul_list[i],":",winArr[i],"балл! Прошел")
    



