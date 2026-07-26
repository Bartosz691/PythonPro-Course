uzytkownicy = [
    {"imie": "Jan", "wiek": 30, "aktywny": True},
    {"imie": "Anna", "wiek": 17, "aktywny": False},
    {"imie": "Piotr", "wiek": 25, "aktywny": True}
]

wynik = [
    uzytkownik["imie"].upper()
    for uzytkownik in uzytkownicy
    if uzytkownik["wiek"] >= 18 and uzytkownik["aktywny"] == True
]

print(wynik)