def loguj(func: callable):
    def wrapper(*args, **kwargs):
         print(f"Uruchamiam funkcję {func.__name__}...")
         res = func(*args, **kwargs)
         print(f"Zakończono funkcję {func.__name__}.")
         return res
    return wrapper

@loguj
def dodaj(a, b):
    return a + b

print(dodaj(2,3))
