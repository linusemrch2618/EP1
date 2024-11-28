import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('V8_incidence.csv', index_col=0, parse_dates=True)
df['Maximum']=df.drop(columns=['Gesamt']).max(axis=1)
df['Mean']=df.drop(columns=['Gesamt', 'Maximum']).mean(axis=1)
df['BundeslandMaxInzidenz'] = df.drop(columns=['Gesamt', 'Maximum', 'Mean']).idxmax(axis=1)

df.plot()
plt.legend(loc='upper left', prop={'size': 7})
plt.show()

df['BundeslandMaxInzidenz'].value_counts().plot.pie()
plt.show()