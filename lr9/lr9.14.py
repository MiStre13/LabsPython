import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
is_equal = np.array_equal(arr1, arr2)

if is_equal == True:
    print("Массивы одинаковы")
else:
    print("Массивы ne одинаковы")

