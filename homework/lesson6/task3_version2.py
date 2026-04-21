def srednia_args(*liczby):
    suma = 0
    licznik = 0
    for liczba in liczby:
        suma += liczba
        licznik += 1
    return suma / licznik

def srednia_kolekcja(liczby):
    suma = 0
    licznik = 0
    for liczba in liczby:
        suma += liczba
        licznik += 1
    return suma / licznik

srednia_args(1, 2, 3, 4, 5, 6)
srednia_kolekcja((1,2,3,4,5,6))