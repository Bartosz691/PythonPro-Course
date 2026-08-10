import threading
import time


def pobierz_dane(id_danych):
    print(f"Pobieranie danych {id_danych}...")
    time.sleep(2)
    print(f"Pobrano dane {id_danych}")


# Wykonanie sekwencyjne
start = time.perf_counter()

for id_danych in range(1, 4):
    pobierz_dane(id_danych)

koniec = time.perf_counter()

print(f"\nCzas sekwencyjny: {koniec - start:.2f} s")


# Wykonanie wielowątkowe
start = time.perf_counter()

watki = []

for id_danych in range(1, 4):
    watek = threading.Thread(
        target=pobierz_dane,
        args=(id_danych,),
    )
    watki.append(watek)
    watek.start()

for watek in watki:
    watek.join()

koniec = time.perf_counter()

print(f"Czas wielowątkowy: {koniec - start:.2f} s")