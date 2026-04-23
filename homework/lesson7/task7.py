import functools

def loguj(fun):
    
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        print(f"Uruchamiam funkcję {fun}...")
        
        result = fun(*args, **kwargs )
        
        print(f"Zakończono funkcję {fun}.")
        return result
    return wrapper

@loguj
def funkcja():
    print("działanie funkcji...")

