import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

query = '''
SELECT  COUNT(id_produktu) as liczba_produktow FROM produkty
    
'''
 
c.execute(query)


wynik = c.fetchone()
print(f"Liczba wszystkich produktów: {wynik}")

conn.close()