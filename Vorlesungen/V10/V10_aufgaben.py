import scipy.constants as const

def search_constants(keyword):
    matches = {key: value for key, value in const.physical_constants.items() if keyword.lower() in key.lower()}
    return matches

def main():
    while True:
        keyword = input("Geben Sie ein Stichwort ein (oder 'exit' zum Beenden): ").strip()
        if keyword.lower() == 'exit':
            break

        matches = search_constants(keyword)
        if not matches:
            print("Keine passenden Naturkonstanten gefunden. Bitte versuchen Sie es erneut.")
            continue

        print("\nGefundene Naturkonstanten:")
        for i, key in enumerate(matches.keys(), 1):
            print(f"{i}. {key}")

        try:
            choice = int(input("\nWählen Sie eine Nummer aus der Liste: ").strip())
            if choice < 1 or choice > len(matches):
                raise ValueError("Ungültige Auswahl.")
        except ValueError as e:
            print(f"Fehler: {e}. Bitte versuchen Sie es erneut.")
            continue

        selected_key = list(matches.keys())[choice - 1]
        value, unit, uncertainty = matches[selected_key]
        print(f"\nBezeichnung: {selected_key}")
        print(f"Wert: {value}")
        print(f"Einheit: {unit}")
        print(f"Fehler: {uncertainty}\n")

if __name__ == "__main__":
    main()