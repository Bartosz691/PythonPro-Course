import sqlite3


def dodaj_ksiazki(ksiazki: list[tuple[str, str, int]]):
    with sqlite3.connect('biblioteka.db') as conn:
        c = conn.cursor()
        c.executemany("INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)",
                    ksiazki)
        conn.commit()