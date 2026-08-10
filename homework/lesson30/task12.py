import multiprocessing
import threading
import time


def obliczenia():
    return sum(i * i for i in range(20_000_000))


def test_sekwencyjny():
    start = time.perf_counter()

    obliczenia()
    obliczenia()

    return time.perf_counter() - start


def test_watki():
    start = time.perf_counter()

    watek1 = threading.Thread(target=obliczenia)
    watek2 = threading.Thread(target=obliczenia)

    watek1.start()
    watek2.start()

    watek1.join()
    watek2.join()

    return time.perf_counter() - start


def test_procesy():
    start = time.perf_counter()

    proces1 = multiprocessing.Process(target=obliczenia)
    proces2 = multiprocessing.Process(target=obliczenia)

    proces1.start()
    proces2.start()

    proces1.join()
    proces2.join()

    return time.perf_counter() - start


if __name__ == "__main__":
    czas_sekwencyjny = test_sekwencyjny()
    czas_watki = test_watki()
    czas_procesy = test_procesy()

    print(f"Sekwencyjnie: {czas_sekwencyjny:.2f} s")
    print(f"Dwa wątki:    {czas_watki:.2f} s")
    print(f"Dwa procesy:  {czas_procesy:.2f} s")

    # W CPythonie kod CPU-bound wykonywany przez wątki jest ograniczany
    # przez GIL, dlatego dwa wątki zwykle nie dają przyspieszenia.
    #
    # Osobne procesy mają własne interpretery Pythona i własne GIL,
    # dlatego mogą wykonywać obliczenia rzeczywiście równolegle
    # na wielu rdzeniach procesora.