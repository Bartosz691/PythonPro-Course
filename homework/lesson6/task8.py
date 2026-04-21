def stworz_profil(imie: str, **dane_kontaktowe):
     print("imie", imie, "dane_kontaktowe", dane_kontaktowe, "type", type(dane_kontaktowe))
    
print("\n" * 2)
stworz_profil("Bartosz", wiek=22, miejscowosc_zamieszkania="Krakow", szkola="srednia")
print("\n" * 2)
stworz_profil("Milena")
print("\n" * 2)
stworz_profil("malwina", ulica_zamieszkania="słoneczna", nr_domu=28)
