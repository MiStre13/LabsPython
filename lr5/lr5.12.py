numbers = [1,2,3,4,5,7,21,49]

filterCount = list(filter(lambda x: x%7==0, numbers))

print(filterCount)