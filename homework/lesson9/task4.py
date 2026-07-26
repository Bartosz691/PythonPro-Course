import json

with open("config.json", "r", encoding="utf-8") as f:
    dane_z_pliku = json.load(f)

print(
    f"Witaj użytkowniku {dane_z_pliku['użytkownik']}! "
    f"Twój motyw to: {dane_z_pliku['motyw']}"
)