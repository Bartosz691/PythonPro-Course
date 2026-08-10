from multiprocessing import Process


def potega(liczba, pot):
    wynik = liczba ** pot
    print(f"{liczba}^{pot} = {wynik}")


if __name__ == "__main__":
    proces = Process(
        target=potega,
        args=(5, 3),
    )

    proces.start()
    proces.join()