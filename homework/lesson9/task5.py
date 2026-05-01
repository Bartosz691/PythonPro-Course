import csv

produkty = [
    {"nazwa": "Mleko", "cena": 3.50}, 
    {"nazwa": "Chleb", "cena": 4.20}
    
    ]

with open("Produkty.csv", "w", newline="", encoding="utf-8") as f:
 writer = csv.DictWriter(f, fieldnames=["nazwa", "cena"], delimiter=';') # Możemy zmienić separator

 writer.writeheader()
 writer.writerows(produkty)