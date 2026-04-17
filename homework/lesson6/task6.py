imie = input("Podaj imię: ")


ilosc = int(input("Podaj ilość: "))

def wielokrotne_powitanie(imie: str, ilosc: int) -> None:
    for _ in range(ilosc):
        print(f"Cześć, {imie}!")
        
print(wielokrotne_powitanie(imie,ilosc))
        
"""
dla wielu imion:

imiona = "ania,kasia,irek,damian"
    for i, imie in enumerate(imiona.split(",")):
        wielokrotne_powitanie(imie, i)

"""
