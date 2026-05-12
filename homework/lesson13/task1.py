import sqlite3



with sqlite3.connect('biblioteka.db') as conn:
    c = conn.cursor()

res = c.execute('''
CREATE TABLE ksiazki (
id_ksiazka INTEGER PRIMARY KEY,
tytul TEXT NOT NULL,
autor TEXT NOT NULL,
rok_wydania INTEGER) ''')

#zatwierdzamy zmiany w bazie danych
conn.commit()
conn.close()

print("Tabela została utworzona.")