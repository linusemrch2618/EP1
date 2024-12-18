import numpy as np
import matplotlib.pyplot as plt

chessboard = np.array([[1., 0., 1., 0., 1., 0., 1., 0.],
                       [0., 1., 0., 1., 0., 1., 0., 1.],
                       [1., 0., 1., 0., 1., 0., 1., 0.],
                       [0., 1., 0., 1., 0., 1., 0., 1.],
                       [1., 0., 1., 0., 1., 0., 1., 0.],
                       [0., 1., 0., 1., 0., 1., 0., 1.],
                       [1., 0., 1., 0., 1., 0., 1., 0.],
                       [0., 1., 0., 1., 0., 1., 0., 1.]])

chessboard[::2, ::2] = 1
chessboard[1::2, 1::2] = 1

plt.imshow(chessboard, cmap='Greys', origin='lower')
plt.colorbar()
plt.show()