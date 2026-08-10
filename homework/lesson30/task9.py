import threading
import time


suma_calkowita = 0
lock = threading.Lock()


def sumuj_fragment(fragment):
    global suma_calkowita

    suma_fragmentu = sum(fragment)

    with lock:
        suma_calkowita += suma_fragmentu


liczby = list(range(10_000_000))

rozmiar = len(liczby) // 4

fragmenty = [
    liczby[0:rozmiar],
    liczby[rozmiar:rozmiar * 2],
    liczby[rozmiar * 2:rozmiar * 3],
    liczby[rozmiar * 3:],
]

start = time.perf_counter()

watki = []

for fragment in fragmenty:
    watek = threading.Thread(
        target=sumuj_fragment,
        args=(fragment,),
    )

    watki.append(watek)
    watek.start()

for watek in watki:
    watek.join()

koniec = time.perf_counter()

print(f"Suma całkowita: {suma_calkowita}")
print(f"Czas: {koniec - start:.2f} s")