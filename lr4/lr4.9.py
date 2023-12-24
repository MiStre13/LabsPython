arr = [2, 1, 4, 3, 6, 5, 7]

for i in range(0, len(arr)-1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)