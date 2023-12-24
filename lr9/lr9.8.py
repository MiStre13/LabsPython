import numpy as np 
chessboard = np.zeros((8,8))

chessboard[1::2, ::2] = 1
chessboard[::2, 1::2] = 1

print(chessboard)