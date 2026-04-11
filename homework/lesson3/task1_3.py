imie = "Bartosz"
wiek = 25
oceny = [3,6,3,4,5]
czy_student = True
srednia_ocen = sum(oceny) / len(oceny)

student = {
    "imie:": imie,
    "wiek:": wiek,
    "sr_ocen":srednia_ocen,
}

print(student)