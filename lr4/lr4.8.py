# arr = [1,2,3,1,4,5]
# count = 0

# for i in range(len(arr)):
#     if arr[i-1] != arr[i]:
#         count += 1

# print("Число различных элементов",count)

arr = [1, 2, 2, 3, 4, 5, 5, 5]
res = []
for elem in arr:
    if elem not in res:
        res.append(elem)
        print(res)

print("Число различных элементов",len(res))