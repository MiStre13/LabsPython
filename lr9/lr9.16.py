import numpy as np

arr = np.array([1, 3, 5, 7, 9])

value = 6

diff = np.abs(arr - value)
closest_index = np.argmin(diff)

closest_num = arr[closest_index]
print(closest_num)
