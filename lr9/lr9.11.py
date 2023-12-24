import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[(arr > 4) & (arr < 7)] *= -1

print(arr)
