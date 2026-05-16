class RejestracjaUzytkownika(Exception):
    def __init__(self, email, haslo):
        self.email = email 
        self.haslo = haslo
        
    def sprawdz_email(email):
        try:
            
            if not isinstance(email, str):
                raise TypeError("Wprowadzona wartość nie jest tekstem. ")
            
            if "@" not in email:
                raise ValueError("Adres e-mail musi zawierać znak @")
            
            print("E-mail jest poprawny")
            return True
        
        except(TypeError, ValueError) as blad:
            print(f"Błąd: {blad}")
            return False

    def sprawdz_haslo(haslo: str):
        try:
           if len(haslo) < 8:
              raise ValueError("Hasło jest za krókie min. 8 znaków")
           
           print("Hasło jest poprawne. ")
           return True
       
        except (TypeError, ValueError) as blad:
            print(f"Błąd: {blad}")
            return False
        
    email = str(input("Podaj adres e-mail: "))
    haslo = str(input ("Podaj hasło: "))
    
    print(sprawdz_email(email))
    print(sprawdz_haslo(haslo))