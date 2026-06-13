import sqlite3

def produkty_powyzej_sredniej():
    
    qr = """
    SELECT nazwa_produktu, cena
    FROM Produkty
    WHERE cena > (
        SELECT AVG(cena)
        FROM Produkty
    )
    """
    with sqlite3.connect('sklep.db') as conn:
        return conn.cursor().execute(qr).fetchall()
    
if __name__ == "__main__":
    for produkt in produkty_powyzej_sredniej():
        print(produkt)