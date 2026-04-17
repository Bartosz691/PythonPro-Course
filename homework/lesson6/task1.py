liczba1 = float(input("Podaj pierwszą liczbę: "))

liczba2 = float(input("Podaj drugą liczbę: "))

znak = input("Podaj znak operacji: ")

def kalkulacja(liczba1: float | int, licba2: float | int, znak: str) -> float|int|str:
    if znak == '+':
        result = liczba1 + liczba2
    elif znak == '-':
        result = liczba1 - liczba2
    elif znak == '*':
        result = liczba1 * liczba2
    elif znak == '/':
        result = liczba1 / liczba2
    else:
        result = "niepoprawny znak"

    return result
     
print(f"wynik działania wynosi: {kalkulacja(liczba1, liczba2, znak)}")