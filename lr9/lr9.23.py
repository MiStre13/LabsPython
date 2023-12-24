import numpy as np

A = np.array([2, 3, 4, 6, 9, 12])

selected_elements = A[(A > 4) & (A % 3 == 0)]

print(selected_elements)
