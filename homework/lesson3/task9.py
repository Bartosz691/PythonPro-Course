a = int(input("Podaj pierwszą wartość logiczną 1 lub 0 "))
b = int(input("Podaj drugą wartość logiczną 1 lub 0 "))

def operacja_and(a,b):
    if a == 1 and b == 1:
        return True
    else:
        return False
    
def operacja_or(a,b):
    if a == 1 or b == 1:
        return True
    else:
        return False
    
if -1 < a < 2 and -1 < b < 2:
    result = operacja_and(a,b)
    result2 = operacja_or(a,b)
    print(f"Wynik operacj AND: {result}")
    print(f"Wynik operacj OR: {result2}")
else:
    print("nie poprawna wartosc logiczna")