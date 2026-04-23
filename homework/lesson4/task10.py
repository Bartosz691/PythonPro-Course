def oblicz_pole_prostokata(A, B):
   
    """
    funkcja wykonuje mnożenie dwóch liczb A i B 
    
    Argumenty:
    
    A - pierwsza liczba
    B- druga liczba
        
    zmienna pole przechowuje wartość pola prostokąta będącego wynikiem mnożenia wartości boków a i b
    funkcja zwraca zmienną pole
    """
    pole = A * B

    return pole

#zmienna bok_a przechowuje wartość boku a
bok_a = 10 

 #zmienna bok_b przechowuje wartość boku b
bok_b = 20

#przypisanie wywołania funkcji do zmiennej wynik
wynik = oblicz_pole_prostokata(bok_a, bok_b)

#wyświetlenie wyniku obliczania pola prostokąta
print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")
           