imiona = ["Anna", "Jan", "Piotr", "Kasia"]

uzytkownik_imie = input("podaj imie: ")

for imie in imiona:
    if imie == uzytkownik_imie.strip().capitalize():
        print("imie znajduje się na liście! ")
        break
else:
    print("Nie znaleziono imienia na liście! ")

licznik = 1
while licznik < 1000:
    print(licznik)
    licznik *= 2