import sqlite3

conn = sqlite3.connect('biblioteka.db')
c = conn.cursor()

c.execute("SELECT * FROM  ksiazki")

# fetchall() pobiera wszystkie pasujące rekordy
wszystkie_ksiazki = c.fetchall()
print("Wszystkie książki w bazie:")
for ksiazka in wszystkie_ksiazki:
 print(ksiazka)
 
 conn.close()