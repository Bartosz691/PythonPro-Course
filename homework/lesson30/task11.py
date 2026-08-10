import queue
import random
import threading
import time


q = queue.Queue()
koniec = threading.Event()


def producent():
    while not koniec.is_set():
        liczba = random.randint(1, 100)
        q.put(liczba)

        print(f"Producent dodał: {liczba}")

        time.sleep(1)


def konsument():
    while not koniec.is_set() or not q.empty():
        try:
            liczba = q.get(timeout=0.5)

            print(f"Konsument pobrał: {liczba}")

            q.task_done()
            time.sleep(1.5)

        except queue.Empty:
            pass


watek_producenta = threading.Thread(target=producent)
watek_konsumenta = threading.Thread(target=konsument)

watek_producenta.start()
watek_konsumenta.start()

time.sleep(10)

koniec.set()

watek_producenta.join()
watek_konsumenta.join()

print("Program zakończył pracę.")