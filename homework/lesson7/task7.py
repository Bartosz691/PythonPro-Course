import functools


def loguj(fun):

    @functools.wraps(fun)
    def wrapper(*args, **kwargs):

        print(f"Uruchamiam funkcję {fun.__name__}...")

        result = fun(*args, **kwargs)

        print(f"Zakończono funkcję {fun.__name__}.")

        return result

    return wrapper


@loguj
def funkcja():
    print("Działanie funkcji...")


funkcja()