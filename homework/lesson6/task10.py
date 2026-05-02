def sprawdz_haslo(haslo: str) -> bool:
 """Sprawdza, czy hasło spełnia wymagania bezpieczeństwa
    
        Warunki:
        -minimum 8 znaków
        -przynajmniej jedna wielka litere
        -przynajmniej ma jedną cyfrę
        
        jeśli warunki są spełnione zwraca wartość True  w przeciwnym wypadku wartość False
    
    """
 ma_min_8 = len(haslo) >= 8 # sprawdza czy hasło zawiera co najmniej 8 znaków
 ma_duza = any(znak.isupper() for znak in haslo) # sprawdza czy hasło zawiera co najmniej jedną wielką literę
 czy_cyfra = any(znak.isdigit() for znak in haslo) # sprawdza czy w haśle występuje co najmniej jedna cyfra
 return ma_min_8 and ma_duza and ma_min_8 and czy_cyfra # zwraca wartość bool funkcji
    
haslo: str = input("Podaj hasło: ") # prosi użytkownika o podanie hasła


print(sprawdz_haslo(haslo)) # wyświetla wywołanie funkcji
