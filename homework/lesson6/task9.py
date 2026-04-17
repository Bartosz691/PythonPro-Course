
n = int(input("Podaj liczbę dla silni: "))

def silnia(n: int) -> int:
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)
    
print(silnia(n))