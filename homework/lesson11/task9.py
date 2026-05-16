class RejestracjaUzytkownika(Exception):
    def __init__(self, email, haslo):
        self.email = email 
        self.haslo = haslo
        
    def sprawdz_email(email):
        try:
            
            if not isinstance(email: str):
                raise TypeError("Wprowadzona wartość nie jest tekstem. ")
            
            if "@" not in email:
                raise ValueError("Adres e-mail musi zawierać znak @")
            
            print("E-mail jest poprawny")
            return True