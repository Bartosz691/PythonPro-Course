import sqlite3

def zwroc_ksiazki():
    with sqlite3.connect('biblioteka.db') as conn:
        c = conn.cursor()
        c.execute("select * from ksiazki")
        return c.fetchall()

def zwroc_ksiazki_autora(autor: str):
    with sqlite3.connect('biblioteka.db') as conn:
        c = conn.cursor()
        c.execute("select * from ksiazki where autor = ?", (autor,))
        return c.fetchall()

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