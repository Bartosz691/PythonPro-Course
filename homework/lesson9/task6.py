import csv

with open("Produkty.csv", "r", encoding="utf-8") as f:
 reader = csv.DictReader(f,  delimiter=';')
 
 sum = 0
 float(sum)
 
 for wiersz in reader:
  cena = wiersz["cena"].replace(',','.')
  sum = sum + float(cena)
  
print("Suma wszystkich cen: ", sum)