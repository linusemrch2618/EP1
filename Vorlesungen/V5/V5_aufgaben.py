import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20}) #Zeichengroesse auf 28 setzten


def wuerfel_becher(wuerfel_in_becher, wuerfel_typ=6):
    result = np.random.randint(1, wuerfel_typ + 1, size=wuerfel_in_becher).sum()
    return result

def multi_wuerfel_becher(anzahl_wuerfe, wuerfel_in_becher=1, wuerfel_typ=6):
    results = np.zeros(anzahl_wuerfe, dtype=int)
    for i in range(anzahl_wuerfe):
        results[i] = wuerfel_becher(wuerfel_in_becher, wuerfel_typ)
    return results

example=multi_wuerfel_becher(1000, 100000, 6)
print(example)

plt.figure()
plt.hist(example, rwidth=0.8)
plt.xlabel('Summe Augenzahl')
plt.ylabel('Häufigkeit')
plt.title('Histogramm')
plt.show()