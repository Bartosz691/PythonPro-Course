import sqlite3

conn = sqlite3.connect('biblioteka.db')
c = conn.cursor()

autor = str(input("Podaj autora książki, którą chcesz zwrócić."))

def zwroc_ksiazki_autora(autor: str):
    with sqlite3.connect('biblioteka.db') as conn:
        c = conn.cursor()
        c.execute("select * from ksiazki where autor = ?", (autor,))
        return c.fetchall()



print (zwroc_ksiazki_autora(autor)) 
  

conn.close()