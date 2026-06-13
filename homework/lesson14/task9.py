import sqlite3

def znajdz_produkty_w_kategorii(nazwa_kategorii):
    
    qr = """
    SELECT p.nazwa_produktu, p.cena
    FROM Produkty AS p
    JOIN Kategorie AS k
        ON p.id_kategorii  = k.id_kategorii
    WHERE k.nazwa_kategorii = ?
    """
    with sqlite3.connect("sklep.db") as conn:
        return conn.cursor().execute(
            qr,
            (nazwa_kategorii,)
            
        ).fetchall()
        
if __name__ == "__main__":
    for produkt in znajdz_produkty_w_kategorii("Elektronika"):
        print(produkt)