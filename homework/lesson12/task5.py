plik = None
zawartosc = ""

try:
    plik = open("nieistniejacy.txt", "r", encoding="utf-8") 
    zawartosc = plik.read()
    
except FileNotFoundError:
     print("Błąd: Plik nie istnieje.")
     print("Zawartość: ", zawartosc)
     
finally: 
    if plik:
        plik.close()
        print("Blok finally: Plik został zamknięty.")
    else:
        print("Blok finally: Nie było nic do zamknięcia")