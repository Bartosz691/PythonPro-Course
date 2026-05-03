uzytkownicy = [
    {"imie": "Jan", "wiek": 30, "aktywny": True},
    {"imie": "Anna", "wiek": 17, "aktywny": False},
    {"imie": "Piotr", "wiek":25, "aktywny": True}
]

pelnoletni_z_duzej = list(filter(lambda u: u["wiek"] >= 18 and u["imie"][0].isupper(),uzytkownicy))

print(pelnoletni_z_duzej)