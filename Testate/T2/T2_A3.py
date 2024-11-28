import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)
y_sin = np.sin(x)
y_taylor = x - (x ** 3) / 6 + (x ** 5) / 120

plt.figure()
plt.plot(x, y_sin, color="black", label="sin")
plt.scatter(x, y_taylor, color="red", label="Taylor", zorder=2)

plt.title("Taylor-Approximation von Sinus um x=0")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()