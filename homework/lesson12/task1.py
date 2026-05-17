from dataclasses import dataclass

@dataclass
class Film:
    tytul: str
    rezyser: str
    rok: int 
    
film1 = Film("Botoks", "Patryk Wega", 2016)
film2 = Film("Star Wars 3", "George Lukas", 2003)

print(film1)
print(film2)