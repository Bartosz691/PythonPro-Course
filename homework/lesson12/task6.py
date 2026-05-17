
haslo = input("Podaj hasło: ")

class InvalidPasswordError(Exception):
   """Wyjątek podnoszony gdy hasło jest niepoprawne""" 
pass

def sprawdz_haslo(haslo):
    dlugosc = len(haslo)
    if dlugosc < 8:
        
        raise InvalidPasswordError("Hasło musi zawierać co najmniej 8 znaków!")
        
try:
    print(sprawdz_haslo(haslo)) 
    print("Poprawnie ustawiono hasło")
except InvalidPasswordError as e:
    print(f"Wystąpił błąd: {e}")
    
