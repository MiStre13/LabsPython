import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_means = np.mean(matrix, axis=1)
matrix_minus_mean = np.subtract(matrix, row_means.reshape(-1, 1))

print(matrix_minus_mean)
