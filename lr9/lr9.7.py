import numpy as np

matrix = np.zeros((5,5), dtype=int)
matrix[1:-1, 1:-1]=1
print(matrix)