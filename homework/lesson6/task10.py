def sprawdz_haslo(haslo: str) -> bool:
    """
    Sprawdza, czy podane hasło spełnia wymagania bezpieczeństwa.

    Warunki:
    - hasło ma co najmniej 8 znaków,
    - zawiera co najmniej jedną wielką literę,
    - zawiera co najmniej jedną cyfrę.

    Args:
        haslo: Hasło przekazane do sprawdzenia.

    Returns:
        True, jeśli wszystkie warunki są spełnione.
        False, jeśli przynajmniej jeden warunek nie jest spełniony.
    """

    ma_min_8 = len(haslo) >= 8
    ma_duza = any(znak.isupper() for znak in haslo)
    ma_cyfre = any(znak.isdigit() for znak in haslo)

    return ma_min_8 and ma_duza and ma_cyfre


haslo = input("Podaj hasło: ")

print(sprawdz_haslo(haslo))