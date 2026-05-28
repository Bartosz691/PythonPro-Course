import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

query = '''
SELECT imie, email  FROM Klienci
    
'''
 
c.execute(query)


wynik = c.fetchall()
print(f"średnia cena produktów z kategorii Książki: {wynik}")

conn.close()