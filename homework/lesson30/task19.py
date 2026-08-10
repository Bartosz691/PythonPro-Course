import random
import time
from concurrent.futures import ThreadPoolExecutor


opinie = [
    "Produkt jest świetny.",
    "Nie jestem zadowolony z zakupu.",
    "Produkt spełnia moje oczekiwania.",
    "Jakość wykonania jest słaba.",
    "Bardzo szybka dostawa.",
    "Produkt jest przeciętny.",
    "Zdecydowanie kupiłbym ponownie.",
    "Nie polecam tego produktu.",
    "Cena jest odpowiednia.",
    "Towar dotarł uszkodzony.",
    "Obsługa była bardzo dobra.",
    "Produkt działa poprawnie.",
    "Spodziewałem się czegoś lepszego.",
    "Jestem bardzo zadowolony.",
    "Produkt nie działa.",
    "Opakowanie było bardzo dobre.",
    "Nie mam zdania o produkcie.",
    "Świetny stosunek ceny do jakości.",
    "Dostawa trwała zbyt długo.",
    "Wszystko zgodne z opisem.",
]


def analizuj_sentyment(zdanie):
    time.sleep(
        random.uniform(0.5, 2.0)
    )

    sentyment = random.choice(
        [
            "Pozytywny",
            "Negatywny",
            "Neutralny",
        ]
    )

    return zdanie, sentyment


start = time.perf_counter()

with ThreadPoolExecutor(
    max_workers=5
) as executor:

    wyniki = list(
        executor.map(
            analizuj_sentyment,
            opinie,
        )
    )

koniec = time.perf_counter()

for zdanie, sentyment in wyniki:
    print(
        f"{sentyment:10} | {zdanie}"
    )

print(
    f"\nCzas analizy: "
    f"{koniec - start:.2f} s"
)