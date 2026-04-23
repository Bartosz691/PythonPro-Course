from functools import reduce

liczby = [1, 2, 3, 4, 5]
wynik = reduce(lambda akumulator, element: akumulator * element, liczby)
print(wynik) 