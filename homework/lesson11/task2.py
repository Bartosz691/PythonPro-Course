class Produkt:
    def __init__(self, cena, kategoria):
        self.cena = cena
        self.kategoria =  kategoria
        
    def _str_(self):
        return f'Cena: "{self.cena}" kategoria: "{self.kategoria}"'
    
prordukt1 = Produkt(5, "długopis")
prordukt2 = Produkt(4.50, "jabłko")

print(prordukt1)
print(prordukt2)