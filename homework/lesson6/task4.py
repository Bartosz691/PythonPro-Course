POZIOM_DOSTEPU = "user"


def zmien_poziom_dostepu():
    POZIOM_DOSTEPU = "admin"

    print(
        "Wartość POZIOM_DOSTEPU wewnątrz funkcji:",
        POZIOM_DOSTEPU
    )


print(
    "Wartość przed wywołaniem funkcji:",
    POZIOM_DOSTEPU
)

zmien_poziom_dostepu()

print(
    "Wartość po wywołaniu funkcji:",
    POZIOM_DOSTEPU
)

# Zmienna POZIOM_DOSTEPU utworzona wewnątrz funkcji jest zmienną lokalną.
# Ma taką samą nazwę jak zmienna globalna, ale jej nie zmienia.
# Dlatego wewnątrz funkcji widzimy "admin", a poza funkcją nadal "user".