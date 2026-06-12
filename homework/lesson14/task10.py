from dataclasses import dataclass, field

import sqlite3

@dataclass
class Produkt:
     
    produkt_id: int
    nazwa_produktu: str
    cena: float
    
def pobierz_wszystkie_produkty():
      
    qr = """
    SELECT id_produktu, nazwa_produktu, cena
    FROM produkty
    """

    with sqlite3.connect("sklep.db") as conn:
        c = conn.cursor()
        c.execute(qr)
        wiersze = c.fetchall()
        
    produkty = []
    
    for wiersz in wiersze:
        produkt = Produkt(
            produkt_id=wiersz[0],
            nazwa_produktu=wiersz[1],
            cena=wiersz[2]
        )
        produkty.append(produkt)
        
    return produkty
    
if __name__ == "__main__": 
  for produkt in pobierz_wszystkie_produkty():
         print(produkt)