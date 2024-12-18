import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd

## A1
z = np.loadtxt('V9_Daten.txt', delimiter=',', skiprows=5)
plt.imshow(z, origin='lower')
print(z)
plt.colorbar()
plt.show()

## A2
x = np.loadtxt('V9_Daten.txt', delimiter=',', skiprows=1, max_rows=1)
y = np.loadtxt('V9_Daten.txt', delimiter=',', skiprows=3, max_rows=1)
X, Y = np.meshgrid(x, y)
ax = plt.axes(projection='3d')
surf = ax.plot_surface(X, Y, z, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth=5)
plt.colorbar(surf)
plt.show()

## A3
pdata = pd.read_excel('V9_daten_pandas.xlsx')
px = pdata.columns[1:].astype(float)
py = pdata.index[1:].astype(float)
pz = pdata.iloc[1:, 1:].values
pX, pY = np.meshgrid(px, py)
ax = plt.axes(projection='3d')
surf = ax.plot_surface(pX, pY, pz, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth=5)
plt.colorbar(surf)
plt.show()