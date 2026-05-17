def bezpieczne_dzielenie(a,b):
    try:
       wynik = a/b
       return wynik
    except ZeroDivisionError:
        
        return f"Błąd nie można dzielić przez zero"


a = float(input("Podaj pierwszą liczbę:"))
b =  float(input("Podaj drugą liczbę:"))

print(bezpieczne_dzielenie(a,b))