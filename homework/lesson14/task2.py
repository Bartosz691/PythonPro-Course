import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

query = '''
SELECT nazwa_produktu, MAX(cena)  FROM produkty
    
'''
 
c.execute(query)


wynik = c.fetchone()
print(f"Nazwa produktu i maksymalna cena: {wynik}")

conn.close()