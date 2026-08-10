from multiprocessing import Pipe, Process


def oblicz_dane(polaczenie):
    liczby = polaczenie.recv()

    suma = sum(liczby)
    srednia = suma / len(liczby)

    polaczenie.send(
        (suma, srednia)
    )

    polaczenie.close()


if __name__ == "__main__":
    rodzic, dziecko = Pipe()

    proces = Process(
        target=oblicz_dane,
        args=(dziecko,),
    )

    proces.start()

    liczby = [10, 20, 30, 40, 50]

    print(f"Proces nadrzędny wysyła: {liczby}")

    rodzic.send(liczby)

    suma, srednia = rodzic.recv()

    print(f"Suma: {suma}")
    print(f"Średnia: {srednia}")

    proces.join()

    rodzic.close()