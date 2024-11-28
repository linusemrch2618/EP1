import random

ergebnis = [0,0]
while sum(ergebnis) != 7:
    ergebnis = [random.randint(1,6) for i in range(2)]
    print("Es wurde {} und {} gewürfelt.".format(ergebnis[0], ergebnis[1]))
