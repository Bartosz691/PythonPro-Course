lista1 = [1, 1]
lista2 = [1, 1]

print("lista1 == lista2:", lista1 == lista2)
print("lista1 is lista2:", lista1 is lista2)

'''Operator == porównuje wartości (zawartość) obiektów.
Obie listy zawierają [1, 1], dlatego lista1 == lista2 zwraca True.
Operator is sprawdza tożsamość obiektów, czyli czy obie zmienne
wskazują dokładnie na ten sam obiekt.
lista1 i lista2 zostały utworzone jako dwie osobne listy,
dlatego lista1 is lista2 zwraca False. '''