def analiza_listy(lista: list[int]) -> tuple[int, int, int]:
    minimum = min(lista)
    maksimum = max(lista)
    suma = sum(lista)

    return minimum, maksimum, suma


liczby = [1, 5, 8, 2, 10, 3]

wynik = analiza_listy(liczby)

print(wynik)