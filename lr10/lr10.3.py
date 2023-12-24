import random  

 
list_size = 15 
L = list(range(list_size)) 
print(L) 
random.shuffle(L) 
print(L) 



def insertionsort(L):
    for i in range(1, len(L)):
        temp = L[i]
        j = i - 1
        while (j >= 0 and temp < L[j]):
            L[j + 1] = L[j]
            j = j - 1
        L[j + 1] = temp
 
insertionsort(L)
print('Сортированный список: ', end='')
print(L)