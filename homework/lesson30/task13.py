import math
import multiprocessing
import random


def czy_pierwsza(liczba):
    if liczba < 2:
        return False

    for dzielnik in range(2, math.isqrt(liczba) + 1):
        if liczba % dzielnik == 0:
            return False

    return True


if __name__ == "__main__":
    liczby = [
        random.randint(1, 1000)
        for _ in range(100)
    ]

    with multiprocessing.Pool() as pool:
        wyniki = pool.map(czy_pierwsza, liczby)

    liczba_pierwszych = sum(wyniki)

    print("Liczby:")
    print(liczby)

    print("\nWyniki True/False:")
    print(wyniki)

    print(f"\nZnaleziono liczb pierwszych: {liczba_pierwszych}")