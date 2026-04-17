tytul = input("Podaj tytuł książki: ")
autor = input("Podaj autora książki: ")
rok_wydania = "2014"

def opis_ksiazki(tytul: str , autor: str, rok_wydania: str | int) -> str:
    ksiazka = tytul + ' '  + autor + ' ' + rok_wydania
    return ksiazka

print(opis_ksiazki(tytul, autor, rok_wydania))