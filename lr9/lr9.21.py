import numpy as np

arr = np.array([5, 2, 8, 1, 4])
n = 3
largest_values = np.sort(arr)[-n:]

print(largest_values)
