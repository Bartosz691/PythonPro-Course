import sqlite3

def zamowienia_anny_nowak():
    
    qr = """
    SELECT p.nazwa_produktu
    FROM Klienci AS k
    JOIN Zamowienia AS z
       ON k.id_klienta = z.id_klienta
    JOIN Zamowienia_Produkty AS zp
       ON z.id_zamowienia = zp.id_zamowienia
    JOIN Produkty AS p
      ON zp.id_produktu = p.id_produktu
    WHERE k.imie = 'Anna Nowak'
    """
    with sqlite3.connect('sklep.db') as conn:
        return conn.cursor().execute(qr).fetchall()
    

if __name__ == "__main__":
    for produkt in zamowienia_anny_nowak():
        print(produkt[0])