class MetaWalidujMetody(type):
    
    def __new__(cls, name, bases, dct):
        
        for nazwa_metody, wartosc in dct.items():
            
            if nazwa_metody.startswith("__"):
                continue
            
            if callable(wartosc):
                
             if wartosc.__doc__ is None:
                    raise TypeError(f"Metoda {nazwa_metody} musi mieć docstring.")
            
            return super().__new__(cls, name, bases, dct)
        
class PoprawnaKlasa(metaclass=MetaWalidujMetody):
     
     def metoda1(self):
         print("Metoda 1")
        
     def metoda2(self):
         print("Metoda 2")
    
     print("PoprawnaKlasa została utworzona poprawnie. ")
     
class NiepoprawnaKlasa(metaclass=MetaWalidujMetody):
    
    def metoda1(self):
        print("Brak docstringa")
        
    def metoda2(self):
        print("Metoda 2")