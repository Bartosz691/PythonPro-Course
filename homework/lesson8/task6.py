from pathlib import Path

def przetworz_dane(dane, klucz):
    log_path = Path("log1.txt")
    
    try:
        return dane[klucz]

    except KeyError as e:

        with open(log_path, "a", encoding="utf-8") as log:
            log.write(f"KeyError: brak klucza {klucz}\n")


        raise Exception(f"Błąd przetwarzania danych - brak klucza: {klucz}") from e



dane = {
    "imie": "Jan",
    "wiek": 30,
    "miasto": "Warszawa"
}

klucz = input("Podaj klucz do odczytu: ")

try:
    wynik = przetworz_dane(dane, klucz)
    print("Wynik:", wynik)

except Exception as e:
    print("Wystąpił błąd:", e)