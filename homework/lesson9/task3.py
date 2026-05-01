import json

konfiguracja = {"użytkownik": "admin",
                "motyw": "ciemny",
                "rozdzielczosc": [1920, 1080]
                }

with open("config.json", "w", encoding="utf-8") as f:
# indent - tworzy ładne wcięcia
# ensure_ascii=False - kluczowe dla polskich znaków!
 json.dump(konfiguracja, f, indent=4, ensure_ascii=False)