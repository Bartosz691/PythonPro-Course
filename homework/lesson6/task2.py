def opis_ksiazki(tytul, autor, rok_wydania=2024):
    return (
        f"Książka '{tytul}' została napisana przez {autor} "
        f"i wydana w roku {rok_wydania}."
    )


# Argumenty pozycyjne
print(opis_ksiazki("Lalka", "Bolesław Prus", 1890))

# Argumenty nazwane
print(
    opis_ksiazki(
        tytul="Pan Tadeusz",
        autor="Adam Mickiewicz",
        rok_wydania=1834
    )
)

# Test wartości domyślnej
print(opis_ksiazki("Nowa książka", "Jan Kowalski"))