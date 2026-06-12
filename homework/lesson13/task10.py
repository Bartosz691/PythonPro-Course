import sqlite3

def znajdz_sale_studenta(nazwisko):
    conn = sqlite3.connect("uczelnia.db")
    c = conn.cursor()
    
    query = """
    SELECT s.imie,
           s.nazwisko,
           a.nazwa_budynku,
           a.numer_sali
    FROM studenci s
    JOIN przypisania p
       ON s.id_studenta = p.id_studenta
    JOIN audytoria a
       ON p.id_audytorium = a.id_audytorium
    WHERE s.nazwisko = ?
    """
    c.execute(query, (nazwisko,))
    wynik = c.fetchone()
    
    if wynik:
        print(
            f"Student {wynik[0]} {wynik[1]} znajduje się w budynku "
            f"{wynik[2]}, sala {wynik[3]}."
        )
    else:
        print("Nie znaleziono studenta.")
        
    conn.close()
    
if __name__ == "__main__":
    znajdz_sale_studenta("Kowalski")