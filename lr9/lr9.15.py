import numpy as np
arr = np.array([1, 2, 3, 4, 5])
max_index = np.argmax(arr)
arr[max_index] = -1
print(arr)
