suma = 0
nazwa = input("Podaj nazwę pliku: ")

try:
    with open(nazwa, "r", encoding="utf-8") as f:
        for linia in f:
            try:
                suma += float(linia.strip())
            except ValueError:
                pass  

except FileNotFoundError:
    print("Plik nie istnieje")

finally:
    print("Suma:", suma)