def analiza_listy(lista: list[int]) -> tuple[float | int]:
    min = None
    max_ = None
    sum_ = 0
    for liczba in lista:
        if min is None or liczba < min:
            min = liczba
        if max_ is None or liczba > max_:
            max_ = liczba
        sum_ += liczba
    
        return min, max_, sum_
 
print(analiza_listy(list(range(10))))
            