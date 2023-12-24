import numpy as np

A = np.random.randint(1, 10, size=(4, 2))
B = np.random.randint(1, 10, size=(2, 5))

print(A)
print(B)

result = np.matmul(A, B)


print(result)
