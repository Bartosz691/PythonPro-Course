tekst = input("Podaj dowolny tekst: ")

czy_prawdziwy = bool(tekst)

print("Wartość bool:", czy_prawdziwy)

if czy_prawdziwy:
    print("Wprowadzony tekst jest prawdziwy (niepusty).")
else:
    print("Wprowadzony tekst jest fałszywy (pusty).")