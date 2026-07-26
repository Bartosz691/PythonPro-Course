kursy = {
    "USD": 4.0,
    "EUR": 4.3
}

while True:
    kwota = float(input("Podaj kwotę w PLN: "))
    waluta = input("Podaj walutę (USD/EUR): ").strip().upper()

    if waluta == "USD":
        wynik = kwota / kursy["USD"]
        print(f"{kwota:.2f} PLN = {wynik:.2f} USD")

    elif waluta == "EUR":
        wynik = kwota / kursy["EUR"]
        print(f"{kwota:.2f} PLN = {wynik:.2f} EUR")

    else:
        print("Niepoprawna waluta.")

    odpowiedz = input("Czy chcesz kontynuować? (tak/nie): ").strip().lower()

    if odpowiedz == "nie":
        break