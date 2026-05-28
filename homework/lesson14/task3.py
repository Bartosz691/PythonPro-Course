import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

query = '''
SELECT SUM(Produkty.cena)  FROM Produkty INNER JOIN Kategorie ON Produkty.id_kategorii = Kategorie.id_kategorii where Kategorie.nazwa_kategorii = "Elektronika"
    
'''
 
c.execute(query)


wynik = c.fetchone()
print(f"Łączna wartość wszystkich produktów z kategorii Elektronika: {wynik}")

conn.close()