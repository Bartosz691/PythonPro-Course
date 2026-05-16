class Pracownik:
    def __init__(self, imie, stawka_godzinowa):
        self.imie = imie
        self.stawka_godzinowa = stawka_godzinowa
       
     
    def oblicz_pensje(self, liczba_godzin):
           return self.stawka_godzinowa * liczba_godzin
       
 
        
class Programista(Pracownik):
    def __init__(self, imie, stawka_godzinowa, jezyki_programowania):
        super().__init__(imie, stawka_godzinowa)
        if isinstance(jezyki_programowania, str):
           jezyki_programowania = [jezyki_programowania]
        self.jezyk_programowania: list = jezyki_programowania
        
   
        
programista = Programista("Janusz",100,["C","C++","Python"])
print(programista.oblicz_pensje(50))

   