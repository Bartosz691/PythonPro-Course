class Pracownik:
    def __init__(self, imie, stawka_godzinowa):
        self.imie = imie
        self.stawka_godzinowa = stawka_godzinowa
        
 
        
class Programista(Pracownik):
    def __init__(self, imie, stawka_godzinowa, jezyki_programowania):
        super().__init__(imie, stawka_godzinowa)
        self.jezyki_programowania = jezyki_programowania
        
    def oblicz_pensje(self, liczba_godzin):
           return self.stawka_godzinowa * liczba_godzin
       
        
programista = Programista()
print(programista.wynik_pensja())

   