import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('V7_Daten.txt', index_col=0)
data.plot(xlim=(0,50))
plt.title('Messdaten')
plt.ylabel('y')
plt.show()