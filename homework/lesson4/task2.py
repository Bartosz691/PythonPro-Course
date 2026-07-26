a, b, c = int("256"), int("256"), int("256")
x, y, z = int("257"), int("257"), int("257")

print(id(a), id(b), id(c))
print(id(x), id(y), id(z))

'''W Pythonie małe liczby całkowite są cache'owane, typowo w zakresie
od -5 do 256. Dlatego zmienne a, b i c mogą wskazywać na ten sam 
istniejący obiekt 256 i mieć takie samo id()

Wartość 257 znajduje się poza typowym zakresem tego cache.
Wywołania int("257") mogą więc utworzyć osobne obiekty reprezentujące
tę samą wartość, dlatego ich id() mogą być różne.
'''