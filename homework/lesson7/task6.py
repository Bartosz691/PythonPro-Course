
licznik = int(0)

def stworz_licznik(czynnik):
 def dodaj(licznik):
     return licznik + czynnik
 return dodaj

zwieksz_o6 = stworz_licznik(6)

print(zwieksz_o6(6))