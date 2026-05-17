class Uzytkownik:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
    
    @property
    def wiek(self):
        print("Odczytano wiek...")
        return self.wiek
    
    @wiek.setter
    def wiek(self, wiek):
        if wiek < 0 or wiek > 120:
            print("Podano nie prawidłową wartość dla wieku")
        else: 
            print(f"podany wiek wynosi: {wiek}")
            
jan = Uzytkownik("Jan", 20)

