cena = 100

czy_student = input("Czy jesteś studentem? (tak/nie): ").strip().lower()
wiek = int(input("Podaj wiek: "))

if (czy_student == "tak" and wiek >= 18) or wiek < 18:
    cena *= 0.5
    print(f"Przysługuje Ci 50% zniżki. Cena biletu: {cena:.2f} PLN")
else:
    print(f"Brak zniżki. Cena biletu: {cena:.2f} PLN")