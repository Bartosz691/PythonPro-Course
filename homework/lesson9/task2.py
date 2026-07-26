from pathlib import Path

plik = input("Podaj nazwę pliku: ")

try:
    with open(plik + ".txt", "r", encoding="utf-8") as f:
        caly_tekst = f.read()
        ilosc_slow = len(caly_tekst.split())

        print(f"Ilość słów w pliku: {ilosc_slow}")

except FileNotFoundError:
    print("Plik nie istnieje")