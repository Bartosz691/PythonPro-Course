import sqlite3

def utworz_tabele_przypisania():
    conn = sqlite3.connect("uczelnia.db")
    c = conn.cursor()
    
    c.execute("""
    CREATE TABLE przypisania (
         id_przypisania INTEGER PRIAMRY KEY,
         id_studenta INTEGER,
         id_audytorium INTEGER,
         FOREIGN KEY (id_studenta) REFERENCES studenci(id_studenta),
         FOREIGN KEY (id_audytorium) REFERENCES audytoria(id_audytorium)
      ) 
        """)
    
    conn.commit()
    conn.close()
    
    print("Tabela przypisania została utworzona.")
    
if __name__ == "__main__":
 utworz_tabele_przypisania()