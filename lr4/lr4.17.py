# array = [[1,10], [2, 20], [3,30], [4,40]]

array = [[i,10*i] for i in range(1,5)]
print(array)
newArray = sum(array,[])
print(newArray)