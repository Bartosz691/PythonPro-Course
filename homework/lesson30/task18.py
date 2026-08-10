import random
import threading


class KontoBankowe:
    def __init__(self, saldo=1000):
        self.saldo = saldo
        self.lock = threading.Lock()

    def wplac(self, kwota):
        with self.lock:
            self.saldo += kwota

            print(
                f"Wpłata: {kwota} zł, "
                f"saldo: {self.saldo} zł"
            )

    def wyplac(self, kwota):
        with self.lock:
            if self.saldo >= kwota:
                self.saldo -= kwota

                print(
                    f"Wypłata: {kwota} zł, "
                    f"saldo: {self.saldo} zł"
                )

            else:
                print(
                    f"Brak środków na wypłatę "
                    f"{kwota} zł"
                )


def wykonaj_wplaty(konto):
    for _ in range(10):
        konto.wplac(
            random.randint(10, 100)
        )


def wykonaj_wyplaty(konto):
    for _ in range(10):
        konto.wyplac(
            random.randint(10, 100)
        )


konto = KontoBankowe(1000)

watki = []

for _ in range(5):
    watki.append(
        threading.Thread(
            target=wykonaj_wplaty,
            args=(konto,),
        )
    )

for _ in range(5):
    watki.append(
        threading.Thread(
            target=wykonaj_wyplaty,
            args=(konto,),
        )
    )

for watek in watki:
    watek.start()

for watek in watki:
    watek.join()

print(f"\nSaldo końcowe: {konto.saldo} zł")