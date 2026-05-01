import json
import os

plik = "zadania.json"

if os.path.exists(plik):
    with open(plik, "r", encoding="utf-8") as f:
        zadania = json.load(f)
        
else:
    zadania = []
    
while True:
    print("\n lista zadań")
    print("1. Dodaj zadanie ")
    print("2. Wyświetl zadania ")
    print("3. Zapisz i wyjdź")

wybor = input("Wybierz opcję: ")

if wybor == "1":
    nowe = input("Podaj treść zadania: ")
    zadania.append(nowe)
    
elif wybor == "2":
    if not zadania:
        print("Brak zadań")
    else:
        print("\nTwoje zadania:")
        for i, zadanie in enumerate(zadania, start=1):
            print(f"{i}.{zadanie}")
            
elif wybor == "3":
    with open(plik, "w", encoding="utf-8") as f:
        json.dump(zadania, f, indent=4, ensure_ascii=False)
    print("Zapisano zadania. Koniec programu.")
    break

else:
    print("Niepoprawnie wybrana opcja ")
   