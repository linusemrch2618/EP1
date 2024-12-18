def float_eingabe():
    while True:
        try:
            return float(input("Geben Sie eine Gleitkomma-Zahl ein: "))
        except ValueError:
            print("Das ist keine Zahl.")

print(float_eingabe())