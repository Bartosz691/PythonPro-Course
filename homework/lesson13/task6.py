import sqlite3

def utworz_tabele():
    conn = sqlite3.connect("uczelnia.db")
    c = conn.cursor()

        
    c.execute("""
    CREATE TABLE studenci (
        id_studenta INTEGER PRIMARY KEY,
        imie TEXT,
        nazwisko TEXT
    )
        """)   
    
    c.execute("""
    CREATE TABLE audytoria (
           id_audytorium INTEGER PRIMARY KEY,
           nazwa_budynku TEXT,
           numer_sali INTEGER
              )
              """)
    conn.commit()
    print("Tabele utworzone")
    
if __name__ == "__main__":
 utworz_tabele()
