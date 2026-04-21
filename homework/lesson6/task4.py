lst = []
print("id po stworzeniu", id(lst))

def funkcja_przekazanie_przez_wskazanie(lista: list):
    """ jakiś opis funkcji
    args:
        linia 2
        linia 3
    """
    print("id wewnatrz listy", id(lista))
    lista.append("x")
    
funkcja_przekazanie_przez_wskazanie(lst)
print("lista po funkcji", lst)
