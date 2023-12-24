import numpy as np


A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 2], [3, 5]])

diff_elements = np.count_nonzero(A != B)


print(f"Отличается в : {diff_elements} элементе")
