'''' int("Python")
Powyższa instrukcja powoduje ValueError, ponieważ funkcja int()
próbuje przekonwertować napis "Python" na liczbę całkowitą.
Napis "Python" nie zawiera zapisu liczby całkowitej, dlatego
Python nie może wykonać takiej konwersji.'''

liczba = int("101")

print(liczba)
