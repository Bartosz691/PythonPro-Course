import functools

def powtorz(n):
    
    def dekorator_wlasciwy(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            wynik = None
            for _ in range(n):
                wynik = func(*args, **kwargs)
            return wynik
        return wrapper
    return dekorator_wlasciwy

@powtorz(3)
def komunikat1(imie):
    print(f"Witaj {imie}")
    
@powtorz(2)
def suma(a,b):
    print(f"suma {a+b}")
    return a+b

print("komunikat 1")
imie = "Bartosz"
print(komunikat1(imie))

print("wywołanie 2")
result = suma(2,2)
