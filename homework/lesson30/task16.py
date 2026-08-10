import hashlib
import multiprocessing
import os


KATALOG = "pliki_hash"


def oblicz_hash(sciezka):
    sha256 = hashlib.sha256()

    with open(sciezka, "rb") as plik:
        while True:
            fragment = plik.read(8192)

            if not fragment:
                break

            sha256.update(fragment)

    return (
        os.path.basename(sciezka),
        sha256.hexdigest(),
    )


if __name__ == "__main__":
    pliki = [
        os.path.join(KATALOG, nazwa)
        for nazwa in os.listdir(KATALOG)
        if os.path.isfile(
            os.path.join(KATALOG, nazwa)
        )
    ]

    with multiprocessing.Pool() as pool:
        wyniki = pool.map(
            oblicz_hash,
            pliki,
        )

    hashe = dict(wyniki)

    for nazwa, hash_pliku in hashe.items():
        print(f"{nazwa}: {hash_pliku}")