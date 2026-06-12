import sqlite3

def dokonaj_przypisan():
    conn = sqlite3.connect("uczelnia.db")
    c = conn.cursor()
    
    przypisania = [
        (1,1),
        (2,2),
        (3,3),
        (4,1)
    ]
    
    c.executemany(
        "INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?)",
        przypisania
    )
    
    conn.commit()
    print(c.execute("SELECT * FROM przypisania").fetchall())
    conn.close()
    
    print("Przypisania zostały dodane.")
    
if __name__ == "__main__":
    dokonaj_przypisan()