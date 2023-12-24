# size = [40,40,41,42,43,43,40,42]
arr = [40,40,41,42,43,43,40,42]
res = []
for elem in arr:
    if elem not in res:
        res.append(elem)
print("Нужны размеры:",res)