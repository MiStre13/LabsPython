def insertionsort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp
 

alist = [3,6,8,2,9,1,7,0,5,9,4] 
insertionsort(alist)
print('Сортированный список: ', end='')
print(alist)