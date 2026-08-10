from multiprocessing import Process, Queue


def wyslij_imie(imie, kolejka):
    kolejka.put(imie)


if __name__ == "__main__":
    kolejka = Queue()

    imie = input("Podaj swoje imię: ")

    proces = Process(
        target=wyslij_imie,
        args=(imie, kolejka),
    )

    proces.start()

    odebrane_imie = kolejka.get()

    proces.join()

    print(f"Witaj, {odebrane_imie}!")