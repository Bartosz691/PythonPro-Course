class BladWalidacjiError(Exception):


    def walidacja_hasla(haslo: str):
        #waliduje hasło
        err_lst = []
        #długość 
        if len(haslo) < 8:
            err_lst.append('hasło za krótkie wymaga minimum 8 znajów.')
    
        if not any(znak.isupper() for znak in haslo):
            err_lst.append('brak dużej litery')
        if not any(znak.isdigit() for znak in haslo):
            err_lst.append('brak cyfry w hasle')
        if any(znak.isalnum() for znak in haslo):
            err_lst.append('brak znaku specjalnego')
        if err_lst:
            raise BladWalidacjiError(*err_lst)    
            

try:
    walidacja_hasla("xd")
except BladWalidacjiError as e:
       # x = 1
       bledy = e
        
    
