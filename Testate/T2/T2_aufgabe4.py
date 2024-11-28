def umrechnung_in_meter(wert: float, einheit="Zoll"):
    if einheit == "Zoll":
        return wert / 39.3701
    elif einheit == "Yard":
        return wert / 1.0936133333333
    else:
        return

print(umrechnung_in_meter(40.0))
print(umrechnung_in_meter(80, 'Zoll'))
print(umrechnung_in_meter(80, 'Yard'))
print(umrechnung_in_meter(80, 'cm'))
