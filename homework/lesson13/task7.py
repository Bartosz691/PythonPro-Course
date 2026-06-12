import sqlite3

def dodaj_dane():
    conn = sqlite3.connect("uczelnia.db")
    c = conn.cursor()
    
    studenci = [
        ("Jan", "Kowalski"),
        ("Anna", "Nowak"),
        ("Piotr", "Wiśniewski"),
        ("Maria", "Zielińska")
    ]
    
    audytoria = [
         ("Bydynek A", 101),
        ("Budynek B", 202),
        ("Budynek C", 303)
   
    ]
    
    c.executemany(
        "INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)",
        studenci
    )
    
    c.executemany(
        "INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)",
        audytoria
    )
    
    conn.commit()
    conn.close()
    
    print("Dane zostały dodane.")
if __name__ == "__main__":
    dodaj_dane()