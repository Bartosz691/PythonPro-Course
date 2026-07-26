class BladWalidacjiError(Exception):
    pass


def walidacja_hasla(haslo: str):
    err_lst = []

    if len(haslo) < 8:
        err_lst.append(
            "Hasło jest za krótkie - wymagane minimum 8 znaków."
        )

    if not any(znak.isupper() for znak in haslo):
        err_lst.append("Brak dużej litery.")

    if not any(znak.isdigit() for znak in haslo):
        err_lst.append("Brak cyfry w haśle.")

    if not any(not znak.isalnum() for znak in haslo):
        err_lst.append("Brak znaku specjalnego.")

    if err_lst:
        raise BladWalidacjiError(err_lst)

    return []


try:
    walidacja_hasla("xd")

except BladWalidacjiError as e:
    bledy = e.args[0]

    print("Błędy walidacji:")

    for blad in bledy:
        print("-", blad)