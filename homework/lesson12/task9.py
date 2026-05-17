from dataclasses import dataclass

class BrakSrodkowError(Exception):
    pass

@dataclass
class KontoBankowe:
    _saldo: float
    wplac: float
    wyplac: float
    
@property
def saldo(self):
    return self._saldo

def wplac(self, kwota):
    if kwota < 0:
        raise ValueError("Nie można wpłacić ujemnej kwoty. ")
     
    self._saldo += kwota
    return f"Wpłacono {kwota} zł"

konto = KontoBankowe(1000,500,200)

try: 
    print("Aktualne saldo: ", konto._saldo)
   
    print("Saldo po wpłacie: ", konto._saldo + konto.wplac ," ile zostało wpłacone: ", konto.wplac)
    
    print("Saldo po wypłacie: ", konto._saldo - konto.wyplac, "ile zostało wypłacone: ", konto.wyplac)
    
except ValueError as e:
    print("Błąd wartości: ", e)
    
except BrakSrodkowError as e:
    print("Błąd", e)
    
finally:
    print("Koniec operacji bankowych")        
    
    