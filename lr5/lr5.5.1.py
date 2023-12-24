array = [1,2,3,4,5]
arrayTwo = [1]

def funcSum(array):
    total = 0 
    for num in array:
        total += num**2
    return total

def fucnSr(array):
    length = len(array)
    total = 0
    for num in array:
        total += num/length
    return total


print(funcSum(array))
print(fucnSr(array))
















