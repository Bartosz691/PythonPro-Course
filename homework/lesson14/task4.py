import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

query = '''
SELECT AVG(Produkty.cena)  FROM Produkty INNER JOIN Kategorie ON Produkty.id_kategorii = Kategorie.id_kategorii where Kategorie.nazwa_kategorii = "Książki"
    
'''
 
c.execute(query)


wynik = c.fetchone()
print(f"średnia cena produktów z kategorii Książki: {wynik}")

conn.close()