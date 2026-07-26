def oblicz_srednia(lista_ocen):
    assert len(lista_ocen) > 0, "Lista ocen nie może być pusta."

    return sum(lista_ocen) / len(lista_ocen)


oceny = [5, 4, 3, 5, 4]

print("Średnia:", oblicz_srednia(oceny))