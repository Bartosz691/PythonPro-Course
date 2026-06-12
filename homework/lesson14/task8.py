import sqlite3

def zadanie8():
    
    qr = """
    SELECT 
        k.nazwa_kategorii AS kategoria, 
        COUNT(p.id_produktu)
    FROM kategorie AS k
    JOIN produkty AS p
          ON p.id_kategorii = k.id_kategorii
    GROUP BY k.id_kategorii, k.nazwa_kategorii
    """
    
    
    with sqlite3.connect('sklep.db') as conn:
        return conn.cursor().execute(qr).fetchall()
    
if __name__ == "__main__":
    for wiersz in zadanie8():
        print(wiersz)
    
   