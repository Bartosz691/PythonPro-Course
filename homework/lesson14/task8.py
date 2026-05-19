import sqlite3

def zadanie8():
    
    qr = """--sql
    SELECT k.nazwa_kategorii as kategoria, count(p.id_produktu)
    from kategorie as k
    join produkty as p
    on p.id_kategorii = k.id_kategorii
    GROUP BY p.id_kategorii 
    """
    
    
    with sqlite3.connect('sklep.db') as conn:
        return conn.cursor().execute(qr).fetchall()
    
if __name__ == "__main__":
    for wiersz in zadanie8():
        print(wiersz)
    
   