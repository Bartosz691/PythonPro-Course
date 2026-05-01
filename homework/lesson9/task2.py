from pathlib import Path
plik = input("podaj nazwę pliku: ")

try:
 with open(plik+".txt", "r", encoding="utf-8") as f:
 # 1. Odczyt całego pliku na raz (dla małych plików)
    caly_tekst = f.read()
    ilosc_slow = len(caly_tekst.split())
    
except FileNotFoundError:
 print("Plik nie istnieje")


print(f"ilość słów w pliku: {ilosc_slow}")