listName = ['Михаил Стрельцов','Василий Акимович']
scoreMath = ['80','90']
scoreRus = ['56','79']
scroreInfo = ['75', '100']


def listScore(x,y,z,v):
    listStudent = []
    for i in range(len(x)):
        listStudent.append(x[i]+','+y[i]+','+z[i]+','+v[i])
    return listStudent


            
print(listScore(listName, scoreMath, scoreRus, scroreInfo))