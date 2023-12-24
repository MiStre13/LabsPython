def insertionsort(L1):
    for i in range(1, len(L1)):
        temp = L1[i]
        j = i - 1
        while (j >= 0 and temp < L1[j]):
            L1[j + 1] = L1[j]
            j = j - 1
        L1[j + 1] = temp
 

L1 = [3,6,8,2,9,1,7,0,5,9,4] 
insertionsort(L1)
print('Сортированный список: ', end='')
print(L1)


def merge_sort(L2): 
    if len(L2) > 1: 
        mid = len(L2)//2
        left = L2[:mid] 
        right = L2[mid:]
        merge_sort(left) 
        merge_sort(right) 
        i = j = k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                L2[k] = left[i] 
                i+=1
            else: 
                L2[k] = right[j] 
                j+=1
            k+=1
        while i < len(left): 
            L2[k] = left[i] 
            i+=1
            k+=1
        while j < len(right): 
            L2[k] = right[j] 
            j+=1
            k+=1

L2 = [3,6,8,2,9,1,7,0,5,9,4]
merge_sort(L2)
print('Сортированный список: ', end='')
print(L2)

  
assert insertionsort(L1) != merge_sort(L2) , "Утверждение ложное"