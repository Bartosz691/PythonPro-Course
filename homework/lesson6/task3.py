n = int(input("Podaj ile liczb: "))


def oblicz_srednia(n: int) -> int|float:
    
    result = 0
    for _ in range(n):
        a = int(input("liczba: "))
        
        result = result + a
    
    if result is None:
        return 0
    else:
        average = result/n
        return average
    
print(oblicz_srednia(n))