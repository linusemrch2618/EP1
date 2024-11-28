import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('V7_Daten.txt', delimiter=',', skiprows=1)

x = data[:, 0]
y_free = data[:, 1]
y_damped = data[:, 2]
y_fast = data[:, 3]

plt.plot(x, y_free, label='free oscillator')
plt.plot(x, y_damped, label='damped oscillator')
plt.plot(x, y_fast , label='fast oscillator')

plt.title('Messdaten')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Anzeigen des Graphen
plt.show()