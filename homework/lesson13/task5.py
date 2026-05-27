
import sqlite3

conn = sqlite3.connect('biblioteka.db')
c = conn.cursor()

def zaktualizuj_rok(autor, tytul, nowy_rok):
    with sqlite3.connect('biblioteka.db') as conn:
        c = conn.cursor()
        c.execute("""UPDATE ksiazki
                  SET rok_wydania = ?
                  WHERE autor = ? and tytul = ?""",
                  (nowy_rok, autor, tytul))
        conn.commit()
        print(c.execute("select * from ksiazki where autor = ? and tytul =  ?",
                        (autor, tytul)).fetchall())


if __name__ == "__main__":
    # print(zwroc_ksiazki(), zwroc_ksiazki_autora('autor2'))
    zaktualizuj_rok("autor1", "ksiazka1", 2026)
    

conn.close()