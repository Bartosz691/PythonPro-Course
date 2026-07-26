class WiekNiepoprawnyError(Exception):
    pass


def rejestruj_uzytkownika(wiek):
    if wiek < 18:
        raise WiekNiepoprawnyError("Wiek jest za niski.")

    print("Rejestracja przebiegła pomyślnie.")


try:
    rejestruj_uzytkownika(15)

except WiekNiepoprawnyError as e:
    print("Jesteś niepełnoletni. Błąd:", e)