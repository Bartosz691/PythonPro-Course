imie = "Bartosz"
wiek = 25
srednia_ocen = [3,2,3,4,5]
czy_student = True

suma_ocen = 0
licznik = 0
for ocena in srednia_ocen:
    suma_ocen += ocena
    licznik = 1 # || licznik = licznik + 1
print(srednia_ocen / licznik)

#opcja2
#srednia_ocen = sum(oceny)/len(oceny)

#opcja3
#def opisz_zmienna(zmienna):
#    return f"{zmienna=}[{zmienna._class_}]"

#for zmienna in (imie, wiek, srednia_ocen, czy_student):
#      print(opisz_zmienna(zmienna))