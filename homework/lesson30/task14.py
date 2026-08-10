import os
import shutil
import threading


KATALOG_ZRODLOWY = "pliki_zrodlowe"
KATALOG_DOCELOWY = "pliki_skopiowane"


def kopiuj_plik(nazwa_pliku):
    zrodlo = os.path.join(
        KATALOG_ZRODLOWY,
        nazwa_pliku,
    )

    cel = os.path.join(
        KATALOG_DOCELOWY,
        nazwa_pliku,
    )

    print(f"Kopiowanie pliku {nazwa_pliku}...")

    shutil.copy2(zrodlo, cel)

    print(f"Ukończono kopiowanie pliku {nazwa_pliku}")


os.makedirs(KATALOG_DOCELOWY, exist_ok=True)

pliki = [
    nazwa
    for nazwa in os.listdir(KATALOG_ZRODLOWY)
    if os.path.isfile(
        os.path.join(KATALOG_ZRODLOWY, nazwa)
    )
]

watki = []

for nazwa_pliku in pliki:
    watek = threading.Thread(
        target=kopiuj_plik,
        args=(nazwa_pliku,),
    )

    watki.append(watek)
    watek.start()

for watek in watki:
    watek.join()

print("Wszystkie pliki zostały skopiowane.")