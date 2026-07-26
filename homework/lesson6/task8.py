def stworz_profil(imie, **dane_dodatkowe):
    profil = {
        "imie": imie
    }

    profil.update(dane_dodatkowe)

    return profil


profil1 = stworz_profil(
    "Bartosz",
    wiek=22,
    miasto="Kraków"
)

profil2 = stworz_profil(
    "Anna",
    wiek=30,
    miasto="Warszawa",
    zawod="Programistka"
)

profil3 = stworz_profil("Jan")

print(profil1)
print(profil2)
print(profil3)