kursy = {"USD": 4.0, "EUR": 4.3}
while True:
    odpowiedz = input("podaj kwote i walute w formacie 'kwora waluta'")
    kwota, waluta = odpowiedz.split()
    if waluta.upper() not in kursy:
        print("Niepoprawna waluta")
        continue
    print(f"{kwota}PLN w {waluta} to {float(kwota) / kursy[waluta.upper()]:.2f}")
    
    if input("czy chcesz zakończyć t/n? ")[0].lower() == "t":
        break