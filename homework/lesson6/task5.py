liczba1: float = float(input("Podaj pierwszą liczbę: ")) # pobiera pierwszą liczbę

liczba2: float = float(input("Podaj drugą liczbę: ")) # pobiera druga liczbę

znak: str = input("Podaj znak operacji: ") # pobiera znak operacji

def kalkulacja(liczba1: float | int, licba2: float | int, znak: str) -> float|int|str:
    """Funkcja pobiera ze zmiennych liczba1 i liczba2 oraz znak wartości liczb na których ma zostać wykonane 
    działanie matematyczne a także wartość tego działania. Następnie wykonuje działanie zgoddne ze wskazanym przez 
    użytkownika zdaniem i zwraca wartość działania w postaci liczby float"""
    
    #sprawdza znak i zgodnie z nim wykonuje zadanie
    if znak == '+':
        result: float = liczba1 + liczba2
    elif znak == '-':
        result: float = liczba1 - liczba2
    elif znak == '*':
        result: float = liczba1 * liczba2
    elif znak == '/':
        result: float = liczba1 / liczba2
    else:
        result = "niepoprawny znak"

    return result
     
print(f"wynik działania wynosi: {kalkulacja(liczba1, liczba2, znak)}") #zwraca wartość działania