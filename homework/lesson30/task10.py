import os
import threading


licznik = 0
lock = threading.Lock()

KATALOG = "pliki_txt"


def policz_slowo(nazwa_pliku, szukane_slowo):
    global licznik

    sciezka = os.path.join(KATALOG, nazwa_pliku)

    with open(sciezka, "r", encoding="utf-8") as plik:
        tekst = plik.read()

    liczba = tekst.lower().split().count(szukane_slowo.lower())

    with lock:
        licznik += liczba

    print(f"{nazwa_pliku}: {liczba}")


szukane_slowo = input("Podaj słowo do wyszukania: ")

pliki = [
    nazwa
    for nazwa in os.listdir(KATALOG)
    if nazwa.endswith(".txt")
]

watki = []

for nazwa_pliku in pliki:
    watek = threading.Thread(
        target=policz_slowo,
        args=(nazwa_pliku, szukane_slowo),
    )

    watki.append(watek)
    watek.start()

for watek in watki:
    watek.join()

print(
    f"Łączna liczba wystąpień słowa "
    f"'{szukane_slowo}': {licznik}"
)