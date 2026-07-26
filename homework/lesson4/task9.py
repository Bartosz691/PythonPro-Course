x = 10
 
print(id(x))

x = x+1
print(id(x))

'''Identyfikator zmienił się ponieważ typ integer w pythonie jest niemutowalny. 
Instrukcja x = x+1 nie modyfikuje istniejącego obiektu 10, lecz powoduje, że zmienna x zaczyna wskazywać na obiekt reprezentujący wartość 11
Funkcja id() zwraca identyfikator obiektu, a nie samej nazwy zmiennej, dlatrgo po zmianie wartości otrzymujemy inne id.'''