class Film:
    def __init__(self, tytul, rezyser, rok_produkcji):
        self.tytul = tytul
        self.rezyser = rezyser
        self.rok_produkcji = rok_produkcji
        
    def informacje(self: str):
        return f'"Tytuł: {self.tytul}" rok produkcji: {self.rok_produkcji} reżyseria: {self.rezyser}"'

film1 = Film("Krytyczna Decyzja", "Stuart Baird", "1996") 
film2 = Film("Avatar: Istota wody", "James Cameron", "2022")

print(film1)
print(film2)