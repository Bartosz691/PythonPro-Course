import multiprocessing
import random
import time


def zastosuj_filtr(obraz):
    return [
        [
            piksel * 1.1
            for piksel in wiersz
        ]
        for wiersz in obraz
    ]


def utworz_obraz():
    return [
        [
            random.random()
            for _ in range(1000)
        ]
        for _ in range(1000)
    ]


if __name__ == "__main__":
    print("Tworzenie 10 obrazów...")

    obrazy = [
        utworz_obraz()
        for _ in range(10)
    ]

    print("Test sekwencyjny...")

    start = time.perf_counter()

    wyniki_sekwencyjne = [
        zastosuj_filtr(obraz)
        for obraz in obrazy
    ]

    czas_sekwencyjny = (
        time.perf_counter() - start
    )

    # tutaj wyniki są usuwane.
    del wyniki_sekwencyjne

    print("Test multiprocessing.Pool...")

    start = time.perf_counter()

    with multiprocessing.Pool() as pool:
        wyniki_rownolegle = pool.map(
            zastosuj_filtr,
            obrazy,
        )

    czas_rownolegly = (
        time.perf_counter() - start
    )

    print(
        f"Czas sekwencyjny: "
        f"{czas_sekwencyjny:.2f} s"
    )

    print(
        f"Czas równoległy: "
        f"{czas_rownolegly:.2f} s"
    )