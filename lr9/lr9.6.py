import numpy as np 
array = np.random.randint(1, 101, size=(12,12))
print(f"Массив: {array}")
maxDigit = array.max()
minDigit = array.min()
print(f"Саммое большое число: {maxDigit}. Самое маленькое число: {minDigit}")