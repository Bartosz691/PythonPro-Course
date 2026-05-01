import json

nazwa_pliku = input("Podaj nazwę pliku, który chcesz otworzyć: ")
fraza = input("Podaj frazę do wyszukiwania: ")

plik_wejsciowy = nazwa_pliku + ".txt"
plik_wyjsciowy = "wyniki_wyszukiwania.txt"

with open(plik_wejsciowy, "r", encoding="utf-8") as f:
    
      with open(plik_wyjsciowy, "w", encoding="utf-8") as f_out:

   
        for linia in f:
           if fraza in linia:
            f_out.write(linia)